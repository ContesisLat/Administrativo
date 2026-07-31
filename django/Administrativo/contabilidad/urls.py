from django.contrib import admin
from django.urls import path
#from .pdfviews import *
#from .excelviews import *
from rest_framework import routers
from .viewsets import *
from desarrollo.viewsets import *
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
route.register('scgvari', ScgvariViewSet),
route.register('scgasct', ScgasctViewSet),
route.register('scgascta', ScgasctaViewSet),
route.register('scgterc', ScgtercViewSet),
route.register('seggere', SegGereViewSet),
route.register('segdept', SegDeptViewSet),
 

urlpatterns = [
    path('segpaag_defaults/', segpaag_defaults, name='segpaag_defaults'),
    path('scgcata', catalogo_cuentas, name='catalogo_cuentas'),
    path('scgcata/valida/', valida_cuentas, name='valida_cuentas'),
    path('scgterc/valida', valida_terceros, name="valida_terceros"),
    path('scggcta/filter', ScggctaFilterView.as_view(), name='scggcta-filter'),
    path('scgsgcta/filter/', ScgsgctaFilterView.as_view(), name='scgsgcta-filter'),
    path('scgtitr/filter/', ScgtitrFilterView.as_view(), name='scgtitr-filter'),
    path('scgscla/filter/', ScgsclaFilterView.as_view(), name='scgscla-filter'),
    path('scgtapl/filter', ScgtaplFilterView.as_view(), name='scgtapl-filter'),
    path('query',query_global, name='query_global'),
    path('querytpy/',query_globaltpy, name='query_globaltpy'),
    path('insert/', InsertView.as_view(), name='insert'),  # Ruta para insertar un nuevo registro
    path('update/', UpdateView.as_view(), name='update'),  # Ruta para actualizar un registro
    path('delete/', DeleteView.as_view(), name='delete'),  # Ruta para eliminar un registro
    path('insertTpy/', InsertViewTpy.as_view(), name='insertTpy'),
    path('updatetpy/', UpdateViewTpy.as_view(), name='updatetpy'),
]
urlpatterns += route.urls