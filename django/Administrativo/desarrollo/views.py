from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from .models import SegUser
import json
from django.core.mail import EmailMessage
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from django.conf import settings
from PIL import Image
from django.db import connection
from pyzbar.pyzbar import decode
from rest_framework import generics
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.db import connections

# Create your views here.

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        usuario = data.get('usuario', '')
        contrasena = data.get('contrasena', '')
        
        # Buscar el usuario en la base de datos 
        try:
            user = SegUser.objects.only('usuario', 'contrasena', 'nombre_usuario').get(usuario=usuario)
        except SegUser.DoesNotExist:
            user = None

        # Verificar contraseña
        if user is not None and user.contrasena == contrasena:
            return JsonResponse({
                'message': 'Autenticacion exitosa',
                'nombre_usuario': user.nombre_usuario  
            })
        else:
            return JsonResponse({'message': 'Credenciales invalidas'}, status=401)
        
    return JsonResponse({'message': request.method}, status=405)

@api_view(['POST'])
def obtener_compania_agencia(request):
    compania = request.data.get('compania')
    agencia = request.data.get('agencia')

    if not compania or not agencia:
        return Response({"error": "Faltan parámetros"}, status=400)

    with connections['default'].cursor() as cursor:
        # Obtener descripción de compañía
        cursor.execute("""
            SELECT descripcion 
            FROM segcomp 
            WHERE compania = %s
        """, [compania])
        comp_row = cursor.fetchone()

        # Obtener descripción de agencia
        cursor.execute("""
            SELECT descripcion 
            FROM segagen 
            WHERE compania = %s AND agencia = %s
        """, [compania, agencia])
        agen_row = cursor.fetchone()

    return Response({
        "compania_desc": comp_row[0] if comp_row else None,
        "agencia_desc": agen_row[0] if agen_row else None
    })


@api_view(['POST'])
def obtener_programas_y_subprogramas(request):
    perfil = request.data.get('perfil')

    if not perfil:
        return Response({"error": "Falta el perfil"}, status=400)

    with connections['default'].cursor() as cursor:

        # 1 Aplicaciones permitidas por perfil
        cursor.execute("""
            SELECT DISTINCT a.aplicacion, a.descripcion
            FROM segaplic a
            INNER JOIN segpape sp 
                ON a.aplicacion = sp.aplicacion
            WHERE sp.perfil = %s
            ORDER BY a.descripcion
        """, [perfil])

        aplicaciones = cursor.fetchall()
        resultado = []

        for aplicacion, desc_aplicacion in aplicaciones:

            # 2 TODOS los procesos de la aplicación
            cursor.execute("""
                SELECT p.proceso, p.descripcion
                FROM segproc p
                WHERE p.aplicacion = %s
                ORDER BY p.descripcion
            """, [aplicacion])

            procesos = cursor.fetchall()
            procesos_list = []

            for proceso, desc_proceso in procesos:

                # 3 Subprogramas autorizados para el perfil
                cursor.execute("""
                    SELECT DISTINCT g.programa, g.descripcion
                    FROM segprog g
                    INNER JOIN segpape sp
                        ON g.programa = sp.programa
                    WHERE sp.perfil = %s
                      AND sp.aplicacion = %s
                      AND sp.proceso = %s
                      AND g.aplicacion = %s
                      AND g.proceso = %s
                      AND (g.status = 'A' OR g.status IS NULL)
                    ORDER BY g.descripcion
                """, [perfil, aplicacion, proceso, aplicacion, proceso])

                subprogramas = cursor.fetchall()

                # Solo mostrar proceso si tiene subprogramas permitidos
                if subprogramas:
                    procesos_list.append({
                        "proceso": desc_proceso,
                        "subprogramas": [
                            {
                                "programa": programa,
                                "descripcion": descripcion
                            }
                            for programa, descripcion in subprogramas
                        ]
                    })

            # Solo mostrar aplicación si tiene procesos válidos
            if procesos_list:
                resultado.append({
                    "aplicacion": desc_aplicacion,
                    "procesos": procesos_list
                })

    return Response(resultado)

@method_decorator(csrf_exempt, name='dispatch')
class EnviarCorreoView(View):
    def post(self, request):
        # Obtener los datos del formulario (correo, mensaje, archivo)
        correo_remitente = request.POST.get('correo_remitente')
        mensaje = request.POST.get('mensaje')
        archivo = request.FILES.get('archivo')  # Obtiene el archivo adjunto si existe
        
        if correo_remitente and mensaje:
            # Crear el correo electrónico
            email = EmailMessage(
                subject="Copadasa",
                body=mensaje,
                from_email=settings.EMAIL_HOST_USER,
                to=['contesispty@gmail.com'],  # Cambia esto por el correo destino
                reply_to=[correo_remitente],  # Opción para responder al remitente
            )

            # Adjuntar archivo si existe
            if archivo:
                email.attach(archivo.name, archivo.read(), archivo.content_type)
            
            try:
                # Enviar el correo
                email.send()
                return JsonResponse({'status': 'success', 'message': 'Correo enviado correctamente'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        else:
            return JsonResponse({'status': 'error', 'message': 'Correo o mensaje no proporcionado'})
        

@api_view(['POST'])
def barcode_reader(request):
    try:
        # Obtener la imagen enviada desde el frontend
        image_file = request.FILES.get('barcode_image')
        
        if not image_file:
            return JsonResponse({'error': 'no se proporciono ningun archivo'}, status=400)

        # Leer la imagen utilizando PIL
        image = Image.open(image_file)

        # Decodificar el código de barras en la imagen
        decoded_objects = decode(image)

        # Si no se encontró ningún código de barras, retornar un error
        if not decoded_objects:
            return JsonResponse({'error': 'No se detecta codigo de barras en la imagen'}, status=400)

        # Extraer la información del código de barras (puede haber más de uno, tomamos el primero)
        barcode_data = decoded_objects[0].data.decode('utf-8')
        barcode_type = decoded_objects[0].type

        # Responder con los datos obtenidos
        return JsonResponse({
            'barcode_data': barcode_data,
            'barcode_type': barcode_type
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@api_view(['POST'])
def query_global(request):
    try:
        # Decodificar el cuerpo de la solicitud para obtener los datos JSON
        data = json.loads(request.body)

        tabla = data.get('tabla')
        filtro = data.get('filtro', {})

        if not tabla:
            return JsonResponse({'error': "Falta el parámetro 'tabla'"}, status=400)

        # Validación: asegúrate de que no haya filtros vacíos en el diccionario
        filtro = {key: value for key, value in filtro.items() if value}  # Elimina claves con valores vacíos

        # Construir la cláusula WHERE de la consulta SQL
        where_clauses = []
        params = []
        for key, value in filtro.items():
            where_clauses.append(f"{key} = %s")
            params.append(value)

        # Construir la consulta SQL dinámica
        sql_query = f"SELECT * FROM {tabla}"
        if where_clauses:
            sql_query += " WHERE " + " AND ".join(where_clauses)

        # Ejecutar la consulta SQL
        with connection.cursor() as cursor:
            cursor.execute(sql_query, params)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # Retornar los resultados como JSON
        return JsonResponse(results, safe=False)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Error al decodificar los datos JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    

class SegUserFilterView(generics.ListAPIView):
    queryset = SegUser.objects.all()
    serializer_class = SegUserSerializer
    filter_backends = [DjangoFilterBackend]  
    filterset_fields = ['nombre_usuario']  