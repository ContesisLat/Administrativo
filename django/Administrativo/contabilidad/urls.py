from django.contrib import admin
from django.urls import path
#from .pdfviews import *
#from .excelviews import *
from rest_framework import routers
from .viewsets import *
from .views import *
from .crud import *

route = routers.SimpleRouter()
route.register('segpaag', SegpaagViewSet),
route.register('scgaage', ScgaageViewSet),
route.register('scgacum', ScgacumViewSet),
route.register('scgafec', ScgafecViewSet),
route.register('scgafed', ScgafedViewSet),
route.register('scgagen', ScgagenViewSet),
route.register('scgcata', ScgcataViewSet),
route.register('scgclas', ScgclasViewSet),
route.register('scgscla', ScgsclaViewSet),
route.register('scgcoac', ScgcoacViewSet),
route.register('scgcocta', ScgcoctaViewSet),
route.register('scgcodi', ScgcodiViewSet),
route.register('scgcolu', ScgcoluViewSet),
route.register('scgctaa', ScgctaaViewSet),
route.register('scgctap', ScgctapViewSet),
route.register('scgdept', ScgdeptViewSet),
route.register('scgeacu', ScgeacuViewSet),
route.register('scgecta', ScgectaViewSet),
route.register('scgesta', ScgestaViewSet),
route.register('scgestc', ScgestcViewSet),
route.register('scggage', ScggageViewSet),
route.register('scggast', ScggastViewSet),
route.register('scggcta', ScggctaViewSet),
route.register('scggint', ScggintViewSet),
route.register('scghiau', ScghiauViewSet),
route.register('scghict', ScghictViewSet),
route.register('scghide', ScghideViewSet),
route.register('scgimpr', ScgimprViewSet),
route.register('scglibr', ScglibrViewSet),
route.register('scglisc', ScgliscViewSet),
route.register('scgmaac', ScgmaacViewSet),
route.register('scgmaad', ScgmaadViewSet),
route.register('scgmayc', ScgmaycViewSet),
route.register('scgmayd', ScgmaydViewSet)
route.register('scgocol', ScgocolViewSet),
route.register('scgpcta', ScgpctaViewSet),
route.register('scgperi', ScgperiViewSet),
route.register('scgperiodo', ScgperiodoViewSet),
route.register('scgsgcta', ScgsgctaViewSet),
route.register('scgsist', ScgsistViewSet),
route.register('scgtapl', ScgtaplViewSet),
route.register('scgtasi', ScgtasiViewSet),
route.register('scgtitr', ScgtitrViewSet),
route.register('scgtran', ScgtranViewSet),
route.register('scgvari', ScgvariViewSet)
 

urlpatterns = [
   path('scgcata', catalogo_cuentas, name='catalogo_cuentas')
    
     
    #path('cardmani/filter', CardmaniFilterView.as_view(), name='cardmani-filter'),
     
    #path('query',query_global, name='query_global'),
    #path('guardar-imagenes',guardar_archivos, name='guardar-imagenes'),
    #path('informe-entrega',informe_entrega, name='informe-entrega'),
    #path('Regmani_excel',excel_regmani,name='Regmani_excel'),
    #path('Caratvue_excel', excel_caratvue, name='Caratvue_excel'),
    #path('Logctmo_excel', excel_logctmo, name="excel_logctmo"),
    #path('AuxLogctmo_excel', excel_auxlogctmo, name="excel_auxlogctmo"),
    #path('Caratvue_excel_resumen', excel_caratvue_resumen, name="excel_caratvue_resumen"),
    #path('Reporte_Ait', excel_reporte_ait, name="excel_reporte_ait"),
    #path('ResCargaOpera', excel_resumen_caropera, name="excel_resumen_caropera"),
    #path('insert/', InsertView.as_view(), name='insert'),  # Ruta para insertar un nuevo registro
    #path('update/', UpdateView.as_view(), name='update'),  # Ruta para actualizar un registro
    #path('delete/', DeleteView.as_view(), name='delete'),  # Ruta para eliminar un registro
]
urlpatterns += route.urls