from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from .serializer import *


class ScgaageViewSet(viewsets.ModelViewSet):
    queryset = Scgaage.objects.all()
    serializer_class = ScgaageSerializer

class ScgacumViewSet(viewsets.ModelViewSet):
    queryset = Scgacum.objects.all()
    serializer_class = ScgacumSerializer

class ScgafecViewSet(viewsets.ModelViewSet):
    queryset = Scgafec.objects.all()
    serializer_class = ScgafecSerializer

class ScgafedViewSet(viewsets.ModelViewSet):
    queryset = Scgafed.objects.all()
    serializer_class = ScgafedSerializer

class ScgagenViewSet(viewsets.ModelViewSet):
    queryset = Scgagen.objects.all()
    serializer_class = ScgagenSerializer

class ScgcataViewSet(viewsets.ModelViewSet):
    queryset = Scgcata.objects.all()
    serializer_class = ScgcataSerializer

class ScgclasViewSet(viewsets.ModelViewSet):
    queryset = Scgclas.objects.all()
    serializer_class = ScgclasSerializer

class ScgsclaViewSet(viewsets.ModelViewSet):
    queryset = Scgscla.objects.all()
    serializer_class = ScgsclaSerializer

class ScgcoacViewSet(viewsets.ModelViewSet):
    queryset = Scgcoac.objects.all()
    serializer_class = ScgcoacSerializer

class ScgcoctaViewSet(viewsets.ModelViewSet):
    queryset = Scgcocta.objects.all()
    serializer_class = ScgcoctaSerializer

class ScgcodiViewSet(viewsets.ModelViewSet):
    queryset = Scgcodi.objects.all()
    serializer_class = ScgcodiSerializer

class ScgcoluViewSet(viewsets.ModelViewSet):
    queryset = Scgcolu.objects.all()
    serializer_class = ScgcoluSerializer

class ScgctaaViewSet(viewsets.ModelViewSet):
    queryset = Scgctaa.objects.all()
    serializer_class = ScgctaaSerializer

class ScgctapViewSet(viewsets.ModelViewSet):
    queryset = Scgctap.objects.all()
    serializer_class = ScgctapSerializer

class ScgdeptViewSet(viewsets.ModelViewSet):
    queryset = Scgdept.objects.all()
    serializer_class = ScgdeptSerializer

class ScgeacuViewSet(viewsets.ModelViewSet):
    queryset = Scgeacu.objects.all()
    serializer_class = ScgeacuSerializer

class ScgectaViewSet(viewsets.ModelViewSet):
    queryset = Scgecta.objects.all()
    serializer_class = ScgectaSerializer

class ScgestaViewSet(viewsets.ModelViewSet):
    queryset = Scgesta.objects.all()
    serializer_class = ScgestaSerializer

class ScgestcViewSet(viewsets.ModelViewSet):
    queryset = Scgestc.objects.all()
    serializer_class = ScgestcSerializer

class ScggageViewSet(viewsets.ModelViewSet):
    queryset = Scggage.objects.all()
    serializer_class = ScggageSerializer

class ScggastViewSet(viewsets.ModelViewSet):
    queryset = Scggast.objects.all()
    serializer_class = ScggastSerializer

class ScggctaViewSet(viewsets.ModelViewSet):
    queryset = Scggcta.objects.all()
    serializer_class = ScggctaSerializer

class ScggintViewSet(viewsets.ModelViewSet):
    queryset = Scggint.objects.all()
    serializer_class = ScggintSerializer

class ScghiauViewSet(viewsets.ModelViewSet):
    queryset = Scghiau.objects.all()
    serializer_class = ScghiauSerializer

class ScghictViewSet(viewsets.ModelViewSet):
    queryset = Scghict.objects.all()
    serializer_class = ScghictSerializer

class ScghideViewSet(viewsets.ModelViewSet):
    queryset = Scghide.objects.all()
    serializer_class = ScghideSerializer

class ScgimprViewSet(viewsets.ModelViewSet):
    queryset = Scgimpr.objects.all()
    serializer_class = ScgimprSerializer

class ScglibrViewSet(viewsets.ModelViewSet):
    queryset = Scglibr.objects.all()
    serializer_class = ScglibrSerializer

class ScgliscViewSet(viewsets.ModelViewSet):
    queryset = Scglisc.objects.all()
    serializer_class = ScgliscSerializer

class ScgmaacViewSet(viewsets.ModelViewSet):
    queryset = Scgmaac.objects.all()
    serializer_class = ScgmaacSerializer 

class ScgmaadViewSet(viewsets.ModelViewSet):
    queryset = Scgmaad.objects.all()
    serializer_class = ScgmaadSerializer

class ScgmaycViewSet(viewsets.ModelViewSet):
    queryset = Scgmayc.objects.all()
    serializer_class = ScgmaycSerializer

class ScgmaydViewSet(viewsets.ModelViewSet):
    queryset = Scgmayd.objects.all()
    serializer_class = ScgmaydSerializer

class ScgocolViewSet(viewsets.ModelViewSet):
    queryset = Scgocol.objects.all()
    serializer_class = ScgocolSerializer

class ScgpctaViewSet(viewsets.ModelViewSet):
    queryset = Scgpcta.objects.all()
    serializer_class = ScgpctaSerializer

class ScgperiViewSet(viewsets.ModelViewSet):
    queryset = Scgperi.objects.all()
    serializer_class = ScgperiSerializer

class ScgperiodoViewSet(viewsets.ModelViewSet):
    queryset = Scgperiodo.objects.all()
    serializer_class = ScgperiodoSerializer

class ScgsgctaViewSet(viewsets.ModelViewSet):
    queryset = Scgsgcta.objects.all()
    serializer_class = ScgsgctaSerializer

class ScgsistViewSet(viewsets.ModelViewSet):
    queryset = Scgsist.objects.all()
    serializer_class = ScgsistSerializer

class ScgtaplViewSet(viewsets.ModelViewSet):
    queryset = Scgtapl.objects.all()
    serializer_class = ScgtaplSerializer

class ScgtasiViewSet(viewsets.ModelViewSet):
    queryset = Scgtasi.objects.all()
    serializer_class = ScgtasiSerializer

class ScgtitrViewSet(viewsets.ModelViewSet):
    queryset = Scgtitr.objects.all()
    serializer_class = ScgtitrSerializer

class ScgtranViewSet(viewsets.ModelViewSet):
    queryset = Scgtran.objects.all()
    serializer_class = ScgtranSerializer

class ScgvariViewSet(viewsets.ModelViewSet):
    queryset = Scgvari.objects.all()
    serializer_class = ScgvariSerializer

class SegpaagViewSet(viewsets.ModelViewSet):
    queryset = Segpaag.objects.all()
    serializer_class = SegpaagSerializer