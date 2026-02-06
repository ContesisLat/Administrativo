from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .viewsets import *
from .views import *
from rest_framework.decorators import api_view
from .crud import *


route = routers.SimpleRouter()
route.register('segerror',SegErrorViewSet)
route.register('segcomp',SegCompViewSet)
route.register('segaplic',SegAplicViewSet)
route.register('seggjer',SegGjerViewSet)
route.register('segperfi',SegPerfiViewSet)
route.register('segbdato',SegBdatoViewSet)
route.register('segprint',SegPrintViewSet)
route.register('segauta',SegAutaViewSet)
route.register('seggere',SegGereViewSet)
route.register('segdept',SegDeptViewSet)
route.register ('seguser',SegUserViewSet)
route.register('segusco',SegUscoViewSet)
route.register('segproc',SegProcViewSet)
route.register('segpara',SegParaViewSet)
route.register('segaperf',SegAperfViewSet)
route.register('segtaut',SegTautViewSet)
route.register('segprog',SegProgViewSet)
route.register('segusat',SegUsatViewSet)
route.register('segjera',SegJeraViewSet)
route.register('segagen',SegAgenViewSet)
route.register('segcapl',SegCaAplViewSet)
route.register('segauco',SegAucoViewSet)
route.register('segpape',SegPapeViewSet)
route.register('segautp',SegAutpViewSet)
route.register('segpprint',SegPprintViewSet)
route.register('segaudd',SegAuddViewSet)
route.register('segaupe',SegAupeViewSet)
route.register('seghusu',SegHusuViewSet)
route.register('segspro',SegSproViewSet)
route.register('segsppe',SegSppeViewSet)
route.register('segausp',SegAuspViewSet)
route.register('segdeta',SegDetaViewSet)
route.register('segaupk',SegAupkViewSet)
route.register('segconm',SegConmViewSet)
route.register('segmain',SegMainViewSet)
route.register('segmaca',SegMacaViewSet)
route.register('segaudc',SegAudcViewSet)
route.register('segayuc',SegAyucViewSet)
route.register('segayud',SegAyudViewSet)
route.register('segaud1',SegAud1ViewSet)
route.register('seggxbo',SegGxboViewSet)
route.register('segucon',SegUconViewSet)
route.register('segfiscal',SegFiscalViewSet)
route.register('seglogin',SegLoginViewSet)
route.register('syslic',SyslicViewSet)
route.register('segrgla',SegRglaViewSet)
route.register('segtcla',SegTclaViewSet)
route.register('segcpas',SegCpasViewSet)
route.register('seghpas',SegHpasViewSet)

urlpatterns = [
    path('seguser/login',api_view(['POST'])(login_view)),
    path('seguser/filter', SegUserFilterView.as_view(), name='seguser-filter'),
    path('envio_correo',EnviarCorreoView.as_view(),name='envio_correo'),
    path('barcode',barcode_reader,name='barcode'),
    path('procesos_subprogramas',obtener_programas_y_subprogramas,name='procesos_subprogramas'),
    path('compania_agencia',obtener_compania_agencia,name='compania_agencia'),
    path('query',query_global, name='query_global'),
    path('insert/', InsertView.as_view(), name='insert'),  # Ruta para insertar un nuevo registro
    path('update/', UpdateView.as_view(), name='update'),  # Ruta para actualizar un registro
    path('delete/', DeleteView.as_view(), name='delete')  # Ruta para eliminar un registro
]
urlpatterns += route.urls
