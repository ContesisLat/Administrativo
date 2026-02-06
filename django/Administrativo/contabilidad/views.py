from django.shortcuts import render

# Create your views here.
import base64
import json
import os
from django.db import connection, connections
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend
import decimal
from django.db.models import Sum
from datetime import date, datetime,time, timedelta
from django.utils import timezone
#from django.db import transaction

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
        with connections['copadasa_db'].cursor() as cursor:
            cursor.execute(sql_query, params)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        # Retornar los resultados como JSON
        return JsonResponse(results, safe=False)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Error al decodificar los datos JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def guardar_archivos(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
 
            matricula_base64 = data.get('matricula')
            cedula_base64 = data.get('cedula')
            firma_base64 = data.get('firma')
            embarque= data.get('no_embarque')
            modificadopor = data.get('modificado_por')
            fechaS = data.get('fecha_status')
            horaS = data.get('hora_status')

            # Ruta base fija donde guardar
            ruta_base = r"/Copadasa"  # Cambia por la ruta real

            # Subcarpetas
            path_matricula = os.path.join(ruta_base, 'matriculas')
            path_cedula = os.path.join(ruta_base, 'cedulas')
            path_firma = os.path.join(ruta_base, 'firmas')

            # Crear carpetas si no existen
            os.makedirs(path_matricula, exist_ok=True)
            os.makedirs(path_cedula, exist_ok=True)
            os.makedirs(path_firma, exist_ok=True)

            # Timestamp único
            timestamp = timezone.localtime(timezone.now()).strftime("%Y-%m-%d-%H%M%S")

            # Guardar matrícula
            if matricula_base64 and "," in matricula_base64:
                data = base64.b64decode(matricula_base64.split(",")[1])
                final_pathM = os.path.join(path_matricula, f"matricula_{timestamp}.png")
                print(final_pathM)
                with open(final_pathM, "wb") as f:
                    f.write(data)

            # Guardar cédula
            if cedula_base64 and "," in cedula_base64:
                data = base64.b64decode(cedula_base64.split(",")[1])
                final_pathC = os.path.join(path_cedula, f"cedula_{timestamp}.png")
                with open(final_pathC, "wb") as f:
                    f.write(data)

            # Guardar firma
            if firma_base64 and "," in firma_base64:
                data = base64.b64decode(firma_base64.split(",")[1])
                final_pathF = os.path.join(path_firma, f"firma_{timestamp}.png")
                with open(final_pathF, "wb") as f:
                    f.write(data)
                    # Ahora final_path contiene la ruta completa del archivo

            #Carentre.objects.filter(no_embarque=embarque).update(modificado_por=modificadopor, fecha_status = fechaS, hora_status = horaS, status = 'F', cedula = final_pathC,
            #                                                    no_placa = final_pathM, firma_digital = final_pathF)
            return JsonResponse({"status": "ok", "mensaje": "Archivos guardados con éxito"})

        except Exception as e:
            import traceback
            print("ERROR al guardar archivos:", e)
            traceback.print_exc() 
            return JsonResponse({"status": "error", "mensaje": str(e)}, status=500)

    return JsonResponse({"status": "error", "mensaje": "Método no permitido"}, status=405)

def catalogo_cuentas(request):
    if request.method == "GET":
        catalogo = Scgcata.objects.all().values()
        try:
            for cata in catalogo:
                if cata['status'] == "A":
                    cata['nom_status'] = "Activo"
                else:
                    cata['nom_status'] = "Inactivo"
               
                
            catalogo_list = list(catalogo)
            return JsonResponse(catalogo_list, safe=False)
        except Scgcata.DoesNotExist:
            return JsonResponse({'Error': 'No pudo cargar el Catalogo'}, status=404)
