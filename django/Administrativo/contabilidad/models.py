from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Scgaage(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    agrupacion = models.SmallIntegerField()
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scgaage'
        unique_together = ('agrupacion', 'compania', 'agencia')

class Scgacum(models.Model):
    code_estado = models.CharField(primary_key=True, max_length=4, null=False)
    acumulador = models.SmallIntegerField(null=False)
    descripcion = models.CharField(max_length=40, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)

    class Meta:
        managed = False
        db_table = 'scgacum'

class Scgafec(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    sistema = models.CharField(max_length=3, null=False)
    no_afectacion = models.IntegerField(null=False)
    fecha_asiento = models.DateField(null=False)
    descripcion = models.CharField(max_length=200)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    no_comprobante = models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgafec'
        unique_together = ('compania', 'agencia', 'sistema', 'no_afectacion')

class Scgafed(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    sistema = models.CharField(max_length=3, null=False)
    no_afectacion = models.IntegerField(null=False)
    no_linea = models.SmallIntegerField(null=False)
    descripcion = models.CharField(max_length=100)
    transaccion = models.CharField(max_length=3, null=False)
    libro = models.CharField(max_length=3)
    tipo_aplica = models.CharField(max_length=4)
    clase = models.CharField(max_length=3)
    subclase = models.CharField(max_length=3)
    cuenta = models.CharField(max_length=20)
    tercero = models.CharField(max_length=6)
    monto_db = models.DecimalField(max_digits=14, decimal_places=2)
    monto_cr = models.DecimalField(max_digits=14, decimal_places=2)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgafed'
        unique_together = ('compania', 'agencia', 'sistema', 'no_afectacion', 'no_linea')
 
class Scgagen(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    clase = models.CharField(max_length=3)
    subclase = models.CharField(max_length=3)
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgagen'
        unique_together = ('compania', 'agencia')

class Scgcata(models.Model):
    cuenta = models.CharField(primary_key=True, max_length=20, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    naturaleza = models.CharField(max_length=1, null=False)
    nivel_cuenta = models.SmallIntegerField(null=False)
    tipo_cuenta = models.CharField(max_length=1, null=False)
    grupo_cuenta = models.CharField(max_length=2)
    recibe = models.CharField(max_length=1)
    aux_interno = models.CharField(max_length=1)
    aux_externo = models.CharField(max_length=1)
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scgcata'

class Scgclas(models.Model):
    tipo_aplica = models.CharField(max_length=4, null=False)
    clase = models.CharField(max_length=3, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgclas'
        unique_together = ('tipo_aplica', 'clase')
        
class Scgscla(models.Model):
    tipo_aplica = models.CharField(max_length=4, null=False)
    clase = models.CharField(max_length=3, null=False)
    subclase = models.CharField(max_length=3, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgscla'
        unique_together = ('tipo_aplica', 'clase', 'subclase')

class Scgcoac(models.Model):
    no_tarea = models.IntegerField(null=False)
    code_estado = models.CharField(max_length=4, null=False)
    columna = models.SmallIntegerField(null=False)
    acumulador = models.SmallIntegerField(null=False)
    valor = models.DecimalField(max_digits=14, decimal_places=2)   

    class Meta:
        managed = False
        db_table = 'scgcoac'
        unique_together = ('no_tarea', 'code_estado', 'columna', 'acumulador')

class Scgcocta(models.Model):
    code_estado = models.CharField(max_length=4, null=False)
    no_linea = models.SmallIntegerField(null=False)
    columna = models.SmallIntegerField(null=False)
    secuencia = models.SmallIntegerField(null=False)
    cuenta_desde = models.CharField(max_length=20)
    cuenta_hasta = models.CharField(max_length=20)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgcocta'
        unique_together = ('code_estado', 'no_linea', 'columna', 'secuencia')

class Scgcodi(models.Model):
    nivel_cuenta = models.SmallIntegerField(primary_key=True, null=False)
    descripcion = models.CharField(max_length=50, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    inicio_cuenta = models.SmallIntegerField(null=False)
    final_cuenta = models.SmallIntegerField(null=False)
    no_posiciones = models.SmallIntegerField(null=False)
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scgcodi'
        
class Scgcolu(models.Model):
    code_estado = models.CharField(max_length=4, null=False)
    columna = models.SmallIntegerField(null=False)
    agrupacion = models.SmallIntegerField()
    titulo = models.CharField(max_length=14)
    tipo_columna = models.CharField(max_length=1)
    tipo_saldos = models.CharField(max_length=1)
    ano_fiscal = models.SmallIntegerField()
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    id = models.AutoField(primary_key=True, null=False)

    class Meta:
        managed = False
        db_table = 'scgcolu'
        unique_together = ('code_estado', 'columna')

class Scgctaa(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    cuenta = models.CharField(max_length=20, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgctaa'
        unique_together = ('compania', 'agencia', 'cuenta')

class Scgctap(models.Model):
    tipo_aplica = models.CharField(primary_key=True, max_length=4, null=False)
    descripcion = models.CharField(max_length=30, null=False)

    class Meta:
        managed = False
        db_table = 'scgctap'

class Scgdept(models.Model):
    compania = models.CharField(max_length=3, null=False)
    gerencia = models.CharField(max_length=2, null=False)
    departamento = models.CharField(max_length=2, null=False)
    clase = models.CharField(max_length=3)
    subclase = models.CharField(max_length=3)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgdept'
        unique_together = ('compania', 'gerencia', 'departamento')

class Scgeacu(models.Model):
    code_estado = models.CharField(max_length=4, null=False)
    no_linea = models.SmallIntegerField(null=False)
    acumulador = models.SmallIntegerField(null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgeacu'
        unique_together = ('code_estado', 'no_linea', 'acumulador')

class Scgecta(models.Model):
    code_estado = models.CharField(max_length=4, null=False)
    no_linea = models.SmallIntegerField(null=False)
    secuencia = models.SmallIntegerField(null=False)
    cuenta_desde = models.CharField(max_length=20)
    cuenta_hasta = models.CharField(max_length=20)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scgecta'
        unique_together = ('code_estado', 'no_linea', 'secuencia')

class Scgesta(models.Model):
    code_estado = models.CharField(primary_key=True, max_length=4, null=False)
    descripcion = models.CharField(max_length=40)
    encabezado_1 = models.CharField(max_length=40)
    encabezado_2 = models.CharField(max_length=60)
    encabezado_3 = models.CharField(max_length=60)
    encabezado_4 = models.CharField(max_length=60)
    tipo_informe = models.CharField(max_length=1)
    naturaleza = models.CharField(max_length=1)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scgesta'

class Scgestc(models.Model):
    code_estado = models.CharField(max_length=4, null=False)
    no_linea = models.SmallIntegerField(null=False)
    tipo_de_linea = models.CharField(max_length=1, null=False)
    sangria = models.SmallIntegerField()
    descripcion = models.CharField(max_length=50)
    terceros = models.CharField(max_length=1)
    acumulador = models.SmallIntegerField()
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgestc'
        unique_together = ('code_estado', 'no_linea')


class Scggage(models.Model):
    agrupacion = models.SmallIntegerField(primary_key=True, null=False)
    descripcion = models.CharField(max_length=40)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scggage'

class Scggast(models.Model):
    ano = models.SmallIntegerField(null=False)
    mes = models.SmallIntegerField(null=False)
    gerencia = models.CharField(max_length=2, null=False)
    depto = models.CharField(max_length=2, null=False)
    rubro = models.CharField(max_length=4, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    monto = models.DecimalField(max_digits=14, decimal_places=2)
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scggast'
        unique_together = ('ano', 'mes', 'gerencia', 'depto', 'rubro')

class Scggaux(models.Model):
    grupo_interno = models.SmallIntegerField(primary_key=True, null=False)
    descripcion = models.CharField(max_length=40, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scggaus'
    
class Scggcta(models.Model):
    tipo_cuenta = models.CharField(primary_key=True, max_length=1, null=False)
    descripcion = models.CharField(max_length=40, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    uso = models.CharField(max_length=1)
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scggcta'

class Scggint(models.Model):
    grupo_interno = models.SmallIntegerField(null=False)
    tercero = models.CharField(max_length=6, null=False)

    class Meta:
        managed = False
        db_table = 'scggint'
        unique_together = ('grupo_interno', 'tercero')

class Scghiau(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    no_asiento = models.IntegerField(null=False)
    fecha_asiento = models.DateField(null=False)
    linea_asiento = models.SmallIntegerField(null=False)
    linea_interno = models.SmallIntegerField(null=False)
    cuenta = models.CharField(max_length=20)
    tercero = models.CharField(max_length=6)
    descripcion = models.CharField(max_length=100)
    tipo_asiento = models.CharField(max_length=1)
    comprobante = models.CharField(max_length=20)
    ano_fiscal = models.SmallIntegerField()
    mes_fiscal = models.SmallIntegerField()
    origen = models.CharField(max_length=3)
    debito = models.DecimalField(max_digits=14, decimal_places=2)
    credito = models.DecimalField(max_digits=14, decimal_places=2)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scghiau'
        unique_together = ('compania', 'agencia', 'no_asiento', 'fecha_asiento', 'linea_asiento', 'linea_interno')

class Scghict(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    no_asiento = models.IntegerField(null=False)
    fecha_asiento = models.DateField(null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    comprobante = models.CharField(max_length=20)
    concepto_asiento = models.CharField(max_length=250)
    monto_balance = models.DecimalField(max_digits=14, decimal_places=2)
    ano_fiscal = models.SmallIntegerField()
    mes_fiscal = models.SmallIntegerField()
    tipo_asiento = models.CharField(max_length=1)
    tipo_comprobante = models.CharField(max_length=3)
    sistema_origen = models.CharField(max_length=3)
    diarizado_por = models.CharField(max_length=10)
    fecha_diario = models.DateField()
    hora_diario = models.TimeField()
    mayorizado_por = models.CharField(max_length=10)
    fecha_mayorizado = models.DateField()
    hora_mayorizado = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scghict'
        unique_together = ('compania', 'agencia', 'no_asiento', 'fecha_asiento')

class Scghide(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    no_asiento = models.IntegerField(null=False)
    fecha_asiento = models.DateField(null=False)
    linea_asiento = models.SmallIntegerField(null=False)
    cuenta = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    tipo_asiento = models.CharField(max_length=1)
    comprobante = models.CharField(max_length=20)
    ano_fiscal = models.SmallIntegerField()
    mes_fiscal = models.SmallIntegerField()
    origen = models.CharField(max_length=3)
    debito = models.DecimalField(max_digits=14, decimal_places=2)
    credito = models.DecimalField(max_digits=14, decimal_places=2)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scghide'
        unique_together = ('compania', 'agencia', 'no_asiento', 'fecha_asiento', 'linea_asiento')

class Scgimpr(models.Model):
    no_tarea = models.IntegerField(null=False)
    code_estado = models.CharField(max_length=4, null=False)
    no_linea = models.SmallIntegerField(name=False)
    columna = models.SmallIntegerField(null=False)
    valor = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'scgimpr'
        unique_together = ('no_tarea', 'code_estado', 'no_linea', 'columna')

class Scglibr(models.Model):
    libro = models.CharField(primary_key=True, max_length=3, null=False)
    tipo_aplica = models.CharField(max_length=4, null=False)
    descripcion = models.CharField(max_length=40, null=False)
    aplica_a = models.CharField(max_length=1)
    auxiliar = models.CharField(max_length=1)
    cuenta = models.CharField(max_length=20)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scglibr'

class Scglisc(models.Model):
    libro = models.CharField(max_length=3, null=False)
    tipo_aplica = models.CharField(max_length=4, null=False)
    clase = models.CharField(max_length=3, null=False)
    subclase = models.CharField(max_length=3, null=False)
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scglisc'
        unique_together = ('libro', 'tipo_aplica', 'clase', 'subclase', 'compania', 'agencia')

class Scgmaac(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    tipo_saldos = models.CharField(max_length=1, null=False)
    ano_fiscal = models.SmallIntegerField(null=False)
    cuenta = models.CharField(max_length=20, null=False)
    tercero = models.CharField(max_length=6, null=False)
    saldo_inicial = models.DecimalField(max_digits=14, decimal_places=2)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgmaac'
        unique_together = ('compania', 'agencia', 'tipo_saldos', 'ano_fiscal', 'cuenta', 'tercero')

class Scgmaad(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    tipo_saldos = models.CharField(max_length=1, null=False)
    ano_fiscal = models.SmallIntegerField(null=False)
    cuenta = models.CharField(max_length=20, null=False)
    tercero = models.CharField(max_length=6, null=False)
    mes_fiscal = models.SmallIntegerField(null=False)
    debito = models.DecimalField(max_digits=14, decimal_places=2)
    credito = models.DecimalField(max_digits=14, decimal_places=2)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgmaad'
        unique_together = ('compania', 'agencia', 'tipo_saldos', 'ano_fiscal', 'cuenta', 'tercero', 'mes_fiscal')

class Scgmayc(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    tipo_saldos = models.CharField(max_length=1, null=False)
    ano_fiscal = models.SmallIntegerField(null=False)
    cuenta = models.CharField(max_length=20, null=False)
    saldo_inicial = models.DecimalField(max_digits=14, decimal_places=2)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgmayc'
        unique_together = ('compania', 'agencia', 'tipo_saldos', 'ano_fiscal', 'cuenta')

class Scgmayd(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    tipo_saldos = models.CharField(max_length=1, null=False)
    ano_fiscal = models.SmallIntegerField(null=False)
    cuenta = models.CharField(max_length=20, null=False)
    mes_fiscal = models.SmallIntegerField(null=False)
    debito = models.DecimalField(max_digits=14, decimal_places=2)
    credito = models.DecimalField(max_digits=14, decimal_places=2)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgmayd'
        unique_together = ('compania', 'agencia', 'tipo_saldos', 'ano_fiscal', 'cuenta', 'mes_fiscal')

class Scgocol(models.Model):
    code_estado = models.CharField(max_length=4, null=False)
    columna = models.SmallIntegerField(null=False)
    secuencia = models.SmallIntegerField(null=False)
    operacion = models.CharField(max_length=1)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgocol'
        unique_together = ('code_estado', 'columna', 'secuencia')

class Scgpcta(models.Model):
    tipo_producto = models.CharField(max_length=3, null=False)
    cuenta = models.CharField(max_length=20,null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgpcta'
        unique_together = ('tipo_producto', 'cuenta')

class Scgperi(models.Model):
    ano_fiscal = models.SmallIntegerField(null=False)
    mes_fiscal = models.SmallIntegerField(null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField() 
    ano_calendario = models.SmallIntegerField()
    mes_calendario = models.SmallIntegerField()
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    tipo_periodo = models.CharField(max_length=1, null=False)
    status = models.CharField(max_length=1, null=False)
    cerrado_por = models.CharField(max_length=10)
    fecha_cierre = models.DateField()
    hora_cierre = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgperi'
        unique_together = ('ano_fiscal', 'mes_fiscal')

class Scgperiodo(models.Model):
    ano_fiscal = models.SmallIntegerField(null=False)
    mes_fiscal = models.SmallIntegerField(null=False)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgperiodo'
        unique_together = ('ano_fiscal', 'mes_fiscal')

class Scgsgcta(models.Model):
    tipo_cuenta = models.CharField(max_length=1, null=False)
    grupo_cuenta = models.CharField(max_length=2, null=False)
    descripcion = models.CharField(max_length=50)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgsgcta'
        unique_together = ('tipo_cuenta', 'grupo_cuenta')

class Scgsist(models.Model):
    sistema = models.CharField(max_length=3, null=False)
    descripcion = models.CharField(max_length=50)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    uso = models.CharField(max_length=1)
    secuencial = models.IntegerField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scgsist'
    
class Scgtapl(models.Model):
    tipo_aplica = models.CharField(primary_key=True, max_length=4, null=False)
    descripcion = models.CharField(max_length=50)
    uso = models.CharField(max_length=4, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scgtapl'
    
class Scgtasi(models.Model):
    tipo_comprobante = models.CharField(primary_key=True, max_length=3, null=False)
    descripcion = models.CharField(max_length=30, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    afecta_periodo = models.CharField(max_length=1, null=False)
    maneja_secuencia = models.CharField(max_length=1)
    secuencial = models.IntegerField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scgtasi'

class Scgtitr(models.Model):
    sistema = models.CharField(max_length=3, null=False)
    transaccion = models.CharField(max_length=3, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgtitr'
        unique_together = ('sistema', 'transaccion')

class Scgtpro(models.Model):
    tipo_producto = models.CharField(primary_key=True, max_length=3, null=False)
    descripcion = models.CharField(max_length=40, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()

    class Meta:
        managed = False
        db_table = 'scgtpro'

class Scgtran(models.Model):
    sistema = models.CharField(max_length=3, null=False)
    transaccion = models.CharField(max_length=3, null=False)
    libro = models.CharField(max_length=3, null=False)
    db_cr = models.CharField(max_length=1, null=False)
    creado_por = models.CharField(max_length=10, null=False)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgtran'
        unique_together = ('sistema', 'transaccion', 'libro', 'db_cr')

class Scgvari(models.Model):
    libro = models.CharField(max_length=3, null=False)
    tipo_aplica = models.CharField(max_length=4, null=False)
    clase = models.CharField(max_length=3, null=False)
    subclase = models.CharField(max_length=3, null=False)
    secuencia = models.SmallIntegerField(null=False)
    tipo_aplica_vari = models.CharField(max_length=4)
    clase_vari = models.CharField(max_length=3)
    subclase_vari = models.CharField(max_length=3)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scgvari'
        unique_together = ('libro', 'tipo_aplica', 'clase', 'subclase', 'secuencia')

class Segpaag(models.Model):
    compania = models.CharField(max_length=3, null=False)
    agencia = models.CharField(max_length=3, null=False)
    aplicacion = models.CharField(max_length=3, null=False)
    parametro = models.CharField(max_length=25, null=False)
    valor = models.CharField(max_length=25, null=False)
    creado_por = models.CharField(max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.TimeField()
    status = models.CharField(max_length=1, null=False)
    modificado_por = models.CharField(max_length=10)
    fecha_status = models.DateField()
    hora_status = models.TimeField()
    fecha = models.DateField()
    hora = models.TimeField()
    id = models.AutoField(primary_key=True, null=False)

    class Meta:
        managed = False
        db_table = 'segpaag'
        unique_together = (('compania', 'agencia', 'aplicacion', 'parametro'),)
