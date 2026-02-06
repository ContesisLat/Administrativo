from rest_framework import serializers  
from .models import *

class SegErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegError
        fields = '__all__'

class SegCompSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegComp
        fields = '__all__'

class SegAplicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAplic
        fields = '__all__'

class SegGjerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegGjer
        fields = '__all__'

class SegPerfiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegPerfi
        fields = '__all__'

class SegBdatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegBdato
        fields = '__all__'

class SegPrintSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegPrint
        fields = '__all__'

class SegAutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAuta
        fields = '__all__'

class SegGereSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegGere
        fields = '__all__'

class SegDeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegDept
        fields = '__all__'

class SegUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegUser
        fields = '__all__'

class SegUscoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegUsco
        fields = '__all__'

class SegProcSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegProc
        fields = '__all__'

class SegParaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegPara
        fields = '__all__'

class SegAperfSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAperf
        fields = '__all__'

class SegTautSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segtaut
        fields = '__all__'

class SegProgSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegProg
        fields = '__all__'

class SegUsatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegUsat
        fields = '__all__'

class SegJeraSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegJera
        fields = '__all__'

class SegAgenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAgen
        fields = '__all__'

class SegCaAplSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegCaApl
        fields = '__all__'

class SegAucoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAuCo
        fields = '__all__'

class SegPapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegPape
        fields = '__all__'

class SegAutpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAutp
        fields = '__all__'

class SegPprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegPprint
        fields = '__all__'

class SegAuddSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAudd
        fields = '__all__'

class SegAupeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAupe
        fields = '__all__'

class SegHusuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seghusu
        fields = '__all__'

class SegSproSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegSpro
        fields = '__all__'

class SegSppeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegSppe
        fields = '__all__'

class SegAuspSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAusp
        fields = '__all__'

class SegDetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segdeta
        fields = '__all__'

class SegAupkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAupk
        fields = '__all__'

class SegConmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegConm
        fields = '__all__'

class SegMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegMain
        fields = '__all__'

class SegMacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segmaca
        fields = '__all__'

class SegAudcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segaudc
        fields = '__all__'

class SegAyucSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegAyuc
        fields = '__all__'

class SegAyudSerializer(serializers.ModelSerializer):
    class Meta:   
        model = SegAyud
        fields = '__all__'

class SegAud1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SegAud1
        fields = '__all__'

class SegGxboSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegGxbo
        fields = '__all__'

class SegUconSerializer(serializers.ModelSerializer):
    class Meta:
        model = SegUcon
        fields = '__all__'

class SegFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segfiscal
        fields = '__all__'

class SegLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seglogin
        fields = '__all__'

class SyslicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syslic
        fields = '__all__'

class SegRglaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segrgla
        fields = '__all__'

class SegTclaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segtcla
        fields = '__all__'

class SegCpasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segcpas
        fields = '__all__'

class SegHpasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seghpas
        fields = '__all__'