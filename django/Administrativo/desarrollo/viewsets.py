from rest_framework import viewsets
from .models import *
from .serializer import *

class SegErrorViewSet(viewsets.ModelViewSet):
    queryset = SegError.objects.all()
    serializer_class = SegErrorSerializer

class SegCompViewSet(viewsets.ModelViewSet):
    queryset = SegComp.objects.all()
    serializer_class = SegCompSerializer

class SegAplicViewSet(viewsets.ModelViewSet):
    queryset = SegAplic.objects.all()
    serializer_class = SegAplicSerializer

class SegGjerViewSet(viewsets.ModelViewSet):
    queryset = SegGjer.objects.all()
    serializer_class = SegGjerSerializer

class SegPerfiViewSet(viewsets.ModelViewSet):
    queryset = SegPerfi.objects.all()
    serializer_class = SegPerfiSerializer

class SegBdatoViewSet(viewsets.ModelViewSet):
    queryset = SegBdato.objects.all()
    serializer_class = SegBdatoSerializer

class SegPrintViewSet(viewsets.ModelViewSet):
    queryset = SegPrint.objects.all()
    serializer_class = SegPrintSerializer

class SegAutaViewSet(viewsets.ModelViewSet):
    queryset = SegAuta.objects.all()
    serializer_class = SegAutaSerializer

class SegGereViewSet(viewsets.ModelViewSet):
    queryset = SegGere.objects.all()
    serializer_class = SegGereSerializer

class SegDeptViewSet(viewsets.ModelViewSet):
    queryset = SegDept.objects.all()
    serializer_class = SegDeptSerializer

class SegUserViewSet(viewsets.ModelViewSet):
    queryset = SegUser.objects.all()
    serializer_class = SegUserSerializer

class SegUscoViewSet(viewsets.ModelViewSet):
    queryset = SegUsco.objects.all()
    serializer_class = SegUscoSerializer

class SegProcViewSet(viewsets.ModelViewSet):
    queryset = SegProc.objects.all()
    serializer_class = SegProcSerializer

class SegParaViewSet(viewsets.ModelViewSet):
    queryset = SegPara.objects.all()
    serializer_class = SegParaSerializer

class SegAperfViewSet(viewsets.ModelViewSet):
    queryset = SegAperf.objects.all()
    serializer_class = SegAperfSerializer

class SegTautViewSet(viewsets.ModelViewSet):
    queryset = Segtaut.objects.all()
    serializer_class = SegTautSerializer

class SegProgViewSet(viewsets.ModelViewSet):
    queryset = SegProg.objects.all()
    serializer_class = SegProgSerializer

class SegUsatViewSet(viewsets.ModelViewSet):
    queryset = SegUsat.objects.all()
    serializer_class = SegUsatSerializer

class SegJeraViewSet(viewsets.ModelViewSet):
    queryset = SegJera.objects.all()
    serializer_class = SegJeraSerializer

class SegAgenViewSet(viewsets.ModelViewSet):
    queryset = SegAgen.objects.all()
    serializer_class = SegAgenSerializer

class SegCaAplViewSet(viewsets.ModelViewSet):
    queryset = SegCaApl.objects.all()
    serializer_class = SegCaAplSerializer

class SegAucoViewSet(viewsets.ModelViewSet):
    queryset = SegAuCo.objects.all()
    serializer_class = SegAucoSerializer

class SegPapeViewSet(viewsets.ModelViewSet):
    queryset = SegPape.objects.all()
    serializer_class = SegPapeSerializer

class SegAutpViewSet(viewsets.ModelViewSet):
    queryset = SegAutp.objects.all()
    serializer_class = SegAutpSerializer

class SegPprintViewSet(viewsets.ModelViewSet):
    queryset = SegPprint.objects.all()
    serializer_class = SegPprintSerializer

class SegAuddViewSet(viewsets.ModelViewSet):
    queryset = SegAudd.objects.all()
    serializer_class = SegAuddSerializer

class SegAupeViewSet(viewsets.ModelViewSet):
    queryset = SegAupe.objects.all()
    serializer_class = SegAupeSerializer

class SegHusuViewSet(viewsets.ModelViewSet):
    queryset = Seghusu.objects.all()
    serializer_class = SegHusuSerializer

class SegSproViewSet(viewsets.ModelViewSet):
    queryset = SegSpro.objects.all()
    serializer_class = SegSproSerializer

class SegSppeViewSet(viewsets.ModelViewSet):
    queryset = SegSppe.objects.all()
    serializer_class = SegSppeSerializer

class SegAuspViewSet(viewsets.ModelViewSet):
    queryset = SegAusp.objects.all()
    serializer_class = SegAuspSerializer

class SegDetaViewSet(viewsets.ModelViewSet):
    queryset = Segdeta.objects.all()
    serializer_class = SegDetaSerializer

class SegAupkViewSet(viewsets.ModelViewSet):
    queryset = SegAupk.objects.all()
    serializer_class = SegAupkSerializer

class SegConmViewSet(viewsets.ModelViewSet):
    queryset = SegConm.objects.all()
    serializer_class = SegConmSerializer

class SegMainViewSet(viewsets.ModelViewSet):
    queryset = SegMain.objects.all()
    serializer_class = SegMainSerializer

class SegMacaViewSet(viewsets.ModelViewSet):
    queryset = Segmaca.objects.all()
    serializer_class = SegMacaSerializer

class SegAudcViewSet(viewsets.ModelViewSet):
    queryset = Segaudc.objects.all()
    serializer_class = SegAudcSerializer

class SegAyucViewSet(viewsets.ModelViewSet):
    queryset = SegAyuc.objects.all()
    serializer_class = SegAyucSerializer

class SegAyudViewSet(viewsets.ModelViewSet):
    queryset = SegAyud.objects.all()
    serializer_class = SegAyudSerializer

class SegAud1ViewSet(viewsets.ModelViewSet):
    queryset = SegAud1.objects.all()
    serializer_class = SegAud1Serializer

class SegGxboViewSet(viewsets.ModelViewSet):
    queryset = SegGxbo.objects.all()    
    serializer_class = SegGxboSerializer

class SegUconViewSet(viewsets.ModelViewSet):
    queryset = SegUcon.objects.all()
    serializer_class = SegUconSerializer

class SegFiscalViewSet(viewsets.ModelViewSet):
    queryset = Segfiscal.objects.all()
    serializer_class = SegFiscalSerializer

class SegLoginViewSet(viewsets.ModelViewSet):
    queryset = Seglogin.objects.all()
    serializer_class = SegLoginSerializer

class SyslicViewSet(viewsets.ModelViewSet):
    queryset = Syslic.objects.all()
    serializer_class = SyslicSerializer

class SegRglaViewSet(viewsets.ModelViewSet):
    queryset = Segrgla.objects.all()
    serializer_class = SegRglaSerializer

class SegTclaViewSet(viewsets.ModelViewSet):
    queryset = Segtcla.objects.all()
    serializer_class = SegTclaSerializer

class SegCpasViewSet(viewsets.ModelViewSet):
    queryset = Segcpas.objects.all()
    serializer_class = SegCpasSerializer

class SegHpasViewSet(viewsets.ModelViewSet):
    queryset = Seghpas.objects.all()
    serializer_class = SegHpasSerializer

    