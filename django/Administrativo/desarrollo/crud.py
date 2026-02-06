from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connections
from .serializer import *
from django.http import JsonResponse

class InsertView(APIView):
    """
    Vista para manejar la inserción de registros en cualquier tabla especificada.
    """

    def post(self, request):
        """
        Maneja las solicitudes POST para insertar un nuevo registro en la base de datos.
        """
        # Obtiene el nombre de la tabla y los datos de la solicitud
        table_name = request.data.get('model')
        fields = request.data.get('data')

        if not table_name or not fields:
            return Response({"error": "Faltan datos o nombre de la tabla"}, status=status.HTTP_400_BAD_REQUEST)

        # Construye la consulta SQL de inserción
        columns = ', '.join(fields.keys())
        placeholders = ', '.join(['%s'] * len(fields))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

       
        try:
            with connections['default'].cursor() as cursor:
                    cursor.execute(sql, list(fields.values()))
            return JsonResponse({"success": True}, status=201)
        except Exception as e:
            print(f"Error during INSERT operation: {str(e)}")
            return JsonResponse({"error": str(e)}, status=400)

  
class UpdateView(APIView):
    """
    Vista para manejar la actualización de registros en cualquier modelo especificado.
    """
    def post(self, request):
        # Obtiene el nombre de la tabla desde la solicitud
        table_name = request.data.get('table')
        filters = request.data.get('filters')
        updated_data = request.data.get('data')

        if not table_name or not filters or not updated_data:
            return Response({"error": "Faltan datos para la operación"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Construir la consulta SQL para la actualización
            set_clause = ', '.join([f"{key} = %s" for key in updated_data.keys()])
            where_clause = ' AND '.join([f"{key} = %s" for key in filters.keys()])

            query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            params = list(updated_data.values()) + list(filters.values())

            # Ejecutar la consulta
            with connections['default'].cursor() as cursor:
                cursor.execute(query, params)

            return Response({"message": "Registro actualizado exitosamente"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Error durante la operación de actualización: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class DeleteView(APIView):
    """
    Vista para manejar la eliminación de registros en cualquier tabla especificada.
    """

    def post(self, request):
        # Obtener datos de la solicitud
        table_name = request.data.get('table')
        filters = request.data.get('filters')  # Diccionario con las condiciones para la eliminación

        if not table_name or not filters:
            return Response({"error": "Faltan datos para la operación"}, status=status.HTTP_400_BAD_REQUEST)

        # Construir la consulta SQL
        where_clause = ' AND '.join([f"{key} = %s" for key in filters.keys()])
        sql_query = f"DELETE FROM {table_name} WHERE {where_clause}"

        params = list(filters.values())

        # Ejecutar la consulta en la base de datos Informix
        try:
            with connections['default'].cursor() as cursor:
                cursor.execute(sql_query, params)
            return Response({"status": "Success"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error during DELETE operation: {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
