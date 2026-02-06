from django.db import models

# Create your models here.
class SegError(models.Model):
    tipo_error = models.CharField(max_length=1)
    no_error = models.SmallIntegerField()
    descripcion = models.CharField(max_length=255)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table = 'segerror'


class SegComp(models.Model):
    compania = models.CharField(primary_key=True, max_length=3)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    direccion_1 = models.CharField(max_length=50, blank=True, null=True)
    direccion_2 = models.CharField(max_length=50, blank=True, null=True)
    direccion_3 = models.CharField(max_length=50, blank=True, null=True)
    ruc = models.CharField(max_length=25, blank=True, null=True)
    dv = models.SmallIntegerField(blank=True, null=True)
    telefono_1 = models.CharField(max_length=15, blank=True, null=True)
    telefono_2 = models.CharField(max_length=15, blank=True, null=True)
    telefono_3 = models.CharField(max_length=15, blank=True, null=True)
    fax_1 = models.CharField(max_length=15, blank=True, null=True)
    fax_2 = models.CharField(max_length=15, blank=True, null=True)
    creado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    hora_creacion = models.TimeField(blank=True, null=True)
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.TimeField(blank=True, null=True)
    apartado = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, null=False)

    class Meta:
        db_table='segcomp'


class SegAplic(models.Model):
    aplicacion = models.CharField(primary_key=True, max_length=3)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, default='A')
    creado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    hora_creacion = models.TimeField(blank=True, null=True)
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.TimeField(blank=True, null=True)

    class Meta:
        db_table ='segaplic'
       

class SegGjer(models.Model):
    grupo_jerarquia = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=50)
    status = models.CharField(max_length=1, default='A')
    creado_por = models.CharField(max_length=10)
    fecha_creacion = models.DateField()
    hora_creacion = models.DateTimeField()
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table='seggjer'
      

class SegPerfi(models.Model):
    perfil = models.SmallIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    status = models.CharField(max_length=1, default='A')
    creado_por = models.CharField(max_length=10)
    fecha_creacion = models.DateField()
    hora_creacion = models.DateTimeField()
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table='segperfi'
        

class SegBdato(models.Model):
    base_datos = models.CharField(max_length=20)
    tipo_base_datos = models.CharField(max_length=1, default='1')
    servidor_bdatos = models.CharField(max_length=20, blank=True, null=True)
    hostname = models.CharField(max_length=20, blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    servicio = models.CharField(max_length=20, blank=True, null=True)
    puerto = models.SmallIntegerField(blank=True, null=True)
    protocolo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table='segbdato'
        

class SegPrint(models.Model):
    impresora = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=30)
    ipaddress = models.CharField(max_length=25, blank=True, null=True)
    dispositivo_unix = models.CharField(max_length=25, blank=True, null=True)
    dispositivo_window = models.CharField(max_length=25, blank=True, null=True)
    creado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    hora_creacion = models.DateTimeField(blank=True, null=True)
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table='segprint'

class SegAuta(models.Model):
    tabla = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50)
    status = models.CharField(max_length=1,default='A')
    creado_por = models.CharField(max_length=10,blank=True,null=True)
    fecha_creacion = models.DateField(blank=True,null=True)
    hora_creacion = models.DateTimeField(blank=True,null=True)
    modificado_por = models.CharField(max_length=10,blank=True,null=True)
    fecha_status = models.DateField(blank=True,null=True)
    hora_status = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table ='segauta'
       

class SegGere(models.Model):
    compania = models.CharField(max_length=3)
    gerencia = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    creado_por = models.CharField(max_length=10,blank=True,null=True)
    fecha_creacion = models.DateField(blank=True,null=True)
    hora_creacion = models.DateTimeField(blank=True,null=True)
    modificado_por = models.CharField(max_length=10,blank=True,null=True)
    fecha_status = models.DateField(blank=True,null=True)
    hora_status = models.DateTimeField(blank=True,null=True)
    status = models.CharField(max_length=1,blank=True,null=True)

    class Meta:
       db_table='seggere'

class SegDept(models.Model):
    compania = models.CharField(max_length=3)
    gerencia = models.CharField(max_length=2)
    departamento = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    creado_por = models.CharField(max_length=10,blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    hora_creacion = models.DateTimeField(blank=True, null=True)
    modificado_por = models.CharField(max_length=10,blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1,blank=True,null=True)

    class Meta:
        db_table='segdept'

class SegUser(models.Model):
    usuario = models.CharField(primary_key=True, max_length=10)
    nombre_usuario = models.CharField(max_length=40)
    contrasena = models.CharField(max_length=10)
    contrasena_apl = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=1, default='A')
    tipo_contrasena = models.CharField(max_length=1, default='1')
    no_de_dias = models.SmallIntegerField(blank=True, null=True)
    ultimo_cambio = models.DateField(blank=True, null=True)
    proximo_cambio = models.DateField(blank=True, null=True)
    avisar_en = models.SmallIntegerField(blank=True, null=True)
    no_tareas = models.SmallIntegerField(blank=True, null=True)
    grupo_jerarquia = models.CharField(max_length=2, blank=True, null=True)
    jerarquia = models.CharField(max_length=2, blank=True, null=True)
    perfil = models.SmallIntegerField(blank=True, null=True)
    compania = models.CharField(max_length=3, blank=True, null=True)
    gerencia = models.CharField(max_length=2, blank=True, null=True)
    departamento = models.CharField(max_length=3, blank=True, null=True)
    correo_elect_1 = models.CharField(max_length=40, blank=True, null=True)
    correo_elect_2 = models.CharField(max_length=40, blank=True, null=True)
    control_horas = models.CharField(max_length=1, default='1', blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_final = models.TimeField(blank=True, null=True)
    creado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    hora_creacion = models.DateTimeField(blank=True, null=True)
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)
    repite_pass = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table='seguser'
      

class SegUsco(models.Model):
    usuario = models.CharField(max_length=10)
    compania = models.CharField(max_length=3)
    agencia = models.CharField(max_length=3)
    status = models.CharField(max_length=1, default='A')
    creado_por = models.CharField(max_length=10,blank=True,null=True)
    fecha_creacion = models.DateField(blank=True,null=True)
    hora_creacion = models.DateTimeField(blank=True,null=True)
    modificado_por = models.CharField(max_length=10,blank=True,null=True)
    fecha_status = models.DateField(blank=True,null=True)
    hora_status = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table='segusco'
      

class SegProc(models.Model):
    aplicacion = models.CharField(max_length=3)
    proceso = models.SmallIntegerField()
    descripcion = models.CharField(max_length=50)
    creado_por = models.CharField(max_length=10,blank=True,null=True)
    fecha_creacion = models.DateField(blank=True,null=True)
    hora_creacion = models.DateTimeField(blank=True,null=True)
    modificado_por = models.CharField(max_length=10,blank=True,null=True)
    fecha_status = models.DateField(blank=True,null=True)
    hora_status = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table='segproc'
        

class SegPara(models.Model):
    aplicacion = models.CharField(max_length=3)
    parametro = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50,blank=True,null=True)
    status = models.CharField(max_length=1, default='A',blank=True,null=True)
    creado_por = models.CharField(max_length=10,blank=True,null=True)
    fecha_creacion = models.DateField(blank=True,null=True)
    hora_creacion = models.DateTimeField(blank=True,null=True)
    modificado_por = models.CharField(max_length=10,blank=True,null=True)
    fecha_status = models.DateField(blank=True,null=True)
    hora_status = models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table='segpara'
        managed = False
        unique_together = (('aplicacion', 'parametro'),)

      

class SegAperf(models.Model):
    perfil = models.SmallIntegerField()
    aplicacion = models.CharField(max_length=3)
    proceso = models.SmallIntegerField()
    autorizado = models.CharField(max_length=1, default='S',blank=True,null=True)
    adicion = models.CharField(max_length=1, default='S', null=True)
    modificacion = models.CharField(max_length=1, default='S', null=True)
    eliminacion = models.CharField(max_length=1, default='S', null=True)
    status = models.CharField(max_length=1, default='A',null=True)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segaperf'
        

class Segtaut(models.Model):
    aplicacion = models.CharField(max_length=3)
    proceso = models.SmallIntegerField()
    tipo_autoriza = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=50)
    maneja_rangos = models.CharField(max_length=1, default='S', null=True)
    creado_por = models.CharField(max_length=10)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segtaut'
      

class SegProg(models.Model):
    programa = models.CharField(primary_key=True, max_length=40)
    descripcion = models.CharField(max_length=50)
    aplicacion = models.CharField(max_length=3, blank=True, null=True)
    proceso = models.SmallIntegerField(blank=True, null=True)
    tipo_autoriza = models.CharField(max_length=2, blank=True, null=True)
    requiere_password = models.CharField(max_length=1, default='S')
    uso_password = models.CharField(max_length=1, blank=True, null=True)
    creado_por = models.CharField(max_length=10)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, null=True)

    class Meta:
        db_table='segprog'
      

class SegUsat(models.Model):
    usuario = models.CharField(max_length=10)
    compania = models.CharField(max_length=3)
    agencia = models.CharField(max_length=3)
    aplicacion = models.CharField(max_length=3)
    proceso = models.SmallIntegerField()
    tipo_autoriza = models.CharField(max_length=2)
    rango_inicial = models.SmallIntegerField(blank=True, null=True)
    rango_final = models.SmallIntegerField(blank=True, null=True)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'segusat'

class SegJera(models.Model):
    grupo_jerarquia = models.CharField(max_length=2)
    jerarquia = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=50)
    status = models.CharField(max_length=1, default='A')
    jerarquia_superior = models.CharField(max_length=2, blank=True, null=True)
    creado_por = models.CharField(max_length=10)
    fecha_creacion = models.DateField()
    hora_creacion = models.DateTimeField()
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table='segjera'
       

class SegAgen(models.Model):
    compania = models.CharField(max_length=3)
    agencia = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    base_datos = models.CharField(max_length=20, blank=True, null=True)
    direccion_1 = models.CharField(max_length=50, blank=True, null=True)
    direccion_2 = models.CharField(max_length=50, blank=True, null=True)
    direccion_3 = models.CharField(max_length=50, blank=True, null=True)
    encargado = models.CharField(max_length=40, blank=True, null=True)
    telefono_1 = models.CharField(max_length=15, blank=True, null=True)
    telefono_2 = models.CharField(max_length=15, blank=True, null=True)
    telefono_3 = models.CharField(max_length=15, blank=True, null=True)
    fax_1 = models.CharField(max_length=15, blank=True, null=True)
    fax_2 = models.CharField(max_length=15, blank=True, null=True)
    creado_por = models.CharField(max_length=10)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.TimeField(null=True)
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=1, null=False)
    id = models.IntegerField(primary_key=True)

    class Meta:
        db_table='segagen'
        unique_together = (('compania', 'agencia'),)

class SegCaApl(models.Model):
    compania = models.CharField(max_length=3)
    agencia = models.CharField(max_length=3)
    aplicacion = models.CharField(max_length=3)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table='segcapl'

class SegAuCo(models.Model):
    tabla = models.CharField(max_length=25)
    columna = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50)
    status = models.CharField(max_length=1, default='A')
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table='segauco'
       

class SegPape(models.Model):
    perfil = models.SmallIntegerField()
    aplicacion = models.CharField(max_length=3)
    proceso = models.SmallIntegerField()
    programa = models.CharField(max_length=40)
    adicion = models.CharField(max_length=1, default='S')
    modificacion = models.CharField(max_length=1, default='S')
    eliminacion = models.CharField(max_length=1, default='S')
    discrimina = models.CharField(max_length=1, default='I')
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10, blank=True, null=True)
    fecha_status = models.DateField(blank=True, null=True)
    hora_status = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table='segpape'
     
class SegAutp(models.Model):
    programa = models.CharField(max_length=40)
    usuario = models.CharField(max_length=10)
    contrasena = models.CharField(max_length=10, null=True, blank=True)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segautp'

class SegPprint(models.Model):
    usuario = models.CharField(max_length=10)
    compania = models.CharField(max_length=3)
    agencia = models.CharField(max_length=3)
    programa = models.CharField(max_length=40)
    impresora = models.CharField(max_length=3)
    status = models.CharField(max_length=1)
    creado_por = models.CharField(max_length=10)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segpprint'

class SegAudd(models.Model):
    no_registro = models.IntegerField()
    tabla = models.CharField(max_length=25)
    columna = models.CharField(max_length=25)
    dato_actual = models.CharField(max_length=50,null=True)
    dato_anterior = models.CharField(max_length=50,null=True)

    class Meta:
        db_table='segaudd'

class SegAupe(models.Model):
    perfil = models.SmallIntegerField()
    aplicacion = models.CharField(max_length=3)
    proceso = models.SmallIntegerField()
    tipo_autoriza = models.CharField(max_length=2)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segaupe'

class Seghusu(models.Model):
    usuario = models.CharField(max_length=10)
    dia_semana = models.CharField(max_length=1)
    discrimina = models.CharField(max_length=1, null=True, blank=True)
    hora_inicio = models.DateTimeField(null=True, blank=True)
    hora_final = models.DateTimeField(null=True, blank=True)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='seghusu'
      

class SegSpro(models.Model):
    programa = models.CharField(max_length=40)
    subprograma = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50,null=True)
    aplicacion = models.CharField(max_length=3,null=True)
    proceso = models.SmallIntegerField(null=True)
    tipo_autoriza = models.CharField(max_length=2,null=True)
    requiere_password = models.CharField(max_length=1,default='N',null=True)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segspro'
       

class SegSppe(models.Model):
    perfil = models.SmallIntegerField()
    aplicacion = models.CharField(max_length=3)
    proceso = models.SmallIntegerField()
    programa = models.CharField(max_length=40)
    subprograma = models.CharField(max_length=20)
    adicion = models.CharField(max_length=1,null=True)
    modificacion = models.CharField(max_length=1,null=True)
    eliminacion = models.CharField(max_length=1,null=True) 
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True) 
    hora_creacion = models.DateTimeField(null=True) 
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segsppe'


class SegAusp(models.Model):
    usuario = models.CharField(max_length=10)
    programa = models.CharField(max_length=40)
    subprograma = models.CharField(max_length=20)
    contrasena = models.CharField(max_length=10,null=True)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segausp'

class Segdeta(models.Model):
    usuario = models.CharField(max_length=10)
    compania = models.CharField(max_length=3)
    agencia = models.CharField(max_length=3)
    aplicacion = models.CharField(max_length=3)
    proceso = models.SmallIntegerField()
    programa = models.CharField(max_length=40)
    subprograma = models.CharField(max_length=20)
    adicion = models.CharField(max_length=1, null=True, blank=True)
    modificacion = models.CharField(max_length=1, null=True, blank=True)
    eliminacion = models.CharField(max_length=1, null=True, blank=True)
    req_contrasena = models.CharField(max_length=1, null=True, blank=True)
    contrasena = models.CharField(max_length=10, null=True, blank=True)
    gerencia = models.CharField(max_length=2, null=True, blank=True)
    departamento = models.CharField(max_length=2, null=True, blank=True)
    grupo_jerarquia = models.CharField(max_length=2, null=True, blank=True)
    jerarquia = models.CharField(max_length=2, null=True, blank=True)
    grupo_jera_sup = models.CharField(max_length=2, null=True, blank=True)
    jerarquia_sup = models.CharField(max_length=2, null=True, blank=True)
    maneja_rango = models.CharField(max_length=1, null=True, blank=True)
    rango_inicial = models.SmallIntegerField(null=True, blank=True)
    rango_final = models.SmallIntegerField(null=True, blank=True)
    con_impresora = models.CharField(max_length=1, null=True, blank=True)
    dispositivo_unix = models.CharField(max_length=25, null=True, blank=True)
    dispositivo_window = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        db_table='segdeta'

class SegAupk(models.Model):
    no_registro = models.IntegerField()
    secuencia = models.SmallIntegerField()
    tabla = models.CharField(max_length=25,null=True)
    columna = models.CharField(max_length=25,null=True)
    valor = models.CharField(max_length=50,null=True)

    class Meta:
        db_table='segaupk'

class SegConm(models.Model):
    usuario = models.CharField(max_length=10)
    compania = models.CharField(max_length=3)
    agencia = models.CharField(max_length=3)
    tabla = models.CharField(max_length=25)
    columna = models.CharField(max_length=25)

    class Meta:
        db_table='segconm'
    
class SegMain(models.Model):
    dominio = models.CharField(max_length=1,default='C')
    tabla = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=1)
    creado_por = models.CharField(max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.DateTimeField()
    modificado_por = models.CharField(max_length=10)
    status = models.CharField(max_length=1,default='A')
    fecha_status = models.DateField()
    hora_status = models.DateTimeField()
    orden_tabla = models.SmallIntegerField(default=0)

    class Meta:
        db_table='segmain'

class Segmaca(models.Model):
    dominio = models.CharField(max_length=1)
    tabla = models.CharField(max_length=25)
    campo = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=50)
    creado_por = models.CharField(max_length=10)
    fecha_creado = models.DateField()
    hora_creado = models.DateTimeField()
    modificado_por = models.CharField(max_length=10)
    status = models.CharField(max_length=1, default='A')
    fecha_status = models.DateField()
    hora_status = models.DateTimeField()

    class Meta:
        db_table='segmaca'
    

class Segaudc(models.Model):
    no_registro = models.AutoField(primary_key=True)
    no_sesion = models.IntegerField(null=True)
    reg_padre = models.IntegerField(null=True)
    tipo_audito = models.SmallIntegerField()
    usuario = models.CharField(max_length=10)
    fecha_inicio = models.DateField()
    hora_inicio = models.DateTimeField(null=True)
    compania = models.CharField(max_length=3,null=True)
    agencia = models.CharField(max_length=3,null=True)
    aplicacion = models.CharField(max_length=3,null=True)
    proceso = models.SmallIntegerField(null=True)
    programa = models.CharField(max_length=40,null=True)
    base_datos = models.CharField(max_length=20,null=True)
    tabla = models.CharField(max_length=25,null=True)
    tipo_actualiza = models.CharField(max_length=1,null=True)
    tipo_autoriza = models.CharField(max_length=2,null=True)
    fecha_final = models.DateField(null=True)
    hora_final = models.DateTimeField(null=True)

    class Meta:
        db_table='segaudc'
     

class SegAyuc(models.Model):
   programa = models.CharField(max_length=40)
   descripcion = models.CharField(max_length=255,null=True)

   class Meta:
       db_table='segayuc'


class SegAyud(models.Model):
    programa = models.CharField(max_length=40)
    secuencia = models.SmallIntegerField()
    campo = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=255,null=True)

    class Meta:
        db_table='segayud'

class SegAud1(models.Model):
    no_registro = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=10,null=True)
    base_datos = models.CharField(max_length=20,null=True)
    tabla = models.CharField(max_length=25,null=True)
    fecha = models.DateField(null=True)
    hora = models.DateTimeField(null=True)
    tipo = models.CharField(max_length=1,null=True)
    no_column01 = models.CharField(max_length=20,null=True)
    dato_actual01 = models.CharField(max_length=255,null=True)
    dato_anteri01 = models.CharField(max_length=255,null=True)
    no_column02 = models.CharField(max_length=20,null=True)
    dato_actual02 = models.CharField(max_length=255,null=True)
    dato_anteri02 = models.CharField(max_length=255,null=True)
    no_column03 = models.CharField(max_length=20,null=True)
    dato_actual03 = models.CharField(max_length=255,null=True)
    dato_anteri03 = models.CharField(max_length=255,null=True)
    no_column04 = models.CharField(max_length=20,null=True)
    dato_actual04 = models.CharField(max_length=255,null=True)
    dato_anteri04 = models.CharField(max_length=255,null=True)
    no_column05 = models.CharField(max_length=20,null=True)
    dato_actual05 = models.CharField(max_length=255,null=True)
    dato_anteri05 = models.CharField(max_length=255,null=True)
    no_column06 = models.CharField(max_length=20,null=True)
    dato_actual06 = models.CharField(max_length=255,null=True)
    dato_anteri06 = models.CharField(max_length=255,null=True)
    no_column07 = models.CharField(max_length=20,null=True)
    dato_actual07 = models.CharField(max_length=255,null=True)
    dato_anteri07 = models.CharField(max_length=255,null=True)
    no_column08 = models.CharField(max_length=20,null=True)
    dato_actual08 = models.CharField(max_length=255,null=True)
    dato_anteri08 = models.CharField(max_length=255,null=True)
    no_column09 = models.CharField(max_length=20,null=True) 
    dato_actual09 = models.CharField(max_length=255,null=True)
    dato_anteri09 = models.CharField(max_length=255,null=True)
    no_column10 = models.CharField(max_length=20,null=True)
    dato_actual10 = models.CharField(max_length=255,null=True)
    dato_anteri10 = models.CharField(max_length=255,null=True) 
    no_column11 = models.CharField(max_length=20,null=True)
    dato_actual11 = models.CharField(max_length=255,null=True)
    dato_anteri11 = models.CharField(max_length=255,null=True)
    no_column12 = models.CharField(max_length=20,null=True)
    dato_actual12 = models.CharField(max_length=255,null=True)
    dato_anteri12 = models.CharField(max_length=255,null=True) 
    no_column13 = models.CharField(max_length=20,null=True)
    dato_actual13 = models.CharField(max_length=255,null=True)
    dato_anteri13 = models.CharField(max_length=255,null=True) 
    no_column14 = models.CharField(max_length=20,null=True)
    dato_actual14 = models.CharField(max_length=255,null=True)
    dato_anteri14 = models.CharField(max_length=255,null=True)
    no_column15 = models.CharField(max_length=20,null=True)
    dato_actual15 = models.CharField(max_length=255,null=True)
    dato_anteri15 = models.CharField(max_length=255,null=True) 
    no_column16 = models.CharField(max_length=20,null=True)
    dato_actual16 = models.CharField(max_length=255,null=True)
    dato_anteri16 = models.CharField(max_length=255,null=True)
    no_column17 = models.CharField(max_length=20,null=True) 
    dato_actual17 = models.CharField(max_length=255,null=True)
    dato_anteri17 = models.CharField(max_length=255,null=True)
    no_column18 = models.CharField(max_length=20,null=True)
    dato_actual18 = models.CharField(max_length=255,null=True) 
    dato_anteri18 = models.CharField(max_length=255,null=True) 
    no_column19 = models.CharField(max_length=20,null=True)
    dato_actual19 = models.CharField(max_length=255,null=True)
    dato_anteri19 = models.CharField(max_length=255,null=True) 
    no_column20 = models.CharField(max_length=20,null=True) 
    dato_actual20 = models.CharField(max_length=255,null=True) 
    dato_anteri20 = models.CharField(max_length=255,null=True) 
    no_column21 = models.CharField(max_length=20,null=True)
    dato_actual21 = models.CharField(max_length=255,null=True) 
    dato_anteri21 = models.CharField(max_length=255,null=True) 
    no_column22 = models.CharField(max_length=20,null=True) 
    dato_actual22 = models.CharField(max_length=255,null=True) 
    dato_anteri22 = models.CharField(max_length=255,null=True) 
    no_column23 = models.CharField(max_length=20,null=True)
    dato_actual23 = models.CharField(max_length=255,null=True)
    dato_anteri23 = models.CharField(max_length=255,null=True) 
    no_column24 = models.CharField(max_length=20,null=True)
    dato_actual24 = models.CharField(max_length=255,null=True) 
    dato_anteri24 = models.CharField(max_length=255,null=True) 
    no_column25 = models.CharField(max_length=20,null=True)
    dato_actual25 = models.CharField(max_length=255,null=True)
    dato_anteri25 = models.CharField(max_length=255,null=True) 
    no_column26 = models.CharField(max_length=20,null=True) 
    dato_actual26 = models.CharField(max_length=255,null=True) 
    dato_anteri26 = models.CharField(max_length=255,null=True) 
    no_column27 = models.CharField(max_length=20,null=True) 
    dato_actual27 = models.CharField(max_length=255,null=True) 
    dato_anteri27 = models.CharField(max_length=255,null=True)
    no_column28 = models.CharField(max_length=20,null=True)
    dato_actual28 = models.CharField(max_length=255,null=True) 
    dato_anteri28 = models.CharField(max_length=255,null=True) 
    no_column29 = models.CharField(max_length=20,null=True) 
    dato_actual29 = models.CharField(max_length=255,null=True) 
    dato_anteri29 = models.CharField(max_length=255,null=True) 
    no_column30 = models.CharField(max_length=20,null=True)
    dato_actual30 = models.CharField(max_length=255,null=True)
    dato_anteri30 = models.CharField(max_length=255,null=True) 
    no_column31 = models.CharField(max_length=20,null=True) 
    dato_actual31 = models.CharField(max_length=255,null=True) 
    dato_anteri31 = models.CharField(max_length=255,null=True) 
    no_column32 = models.CharField(max_length=20,null=True) 
    dato_actual32 = models.CharField(max_length=255,null=True) 
    dato_anteri32 = models.CharField(max_length=255,null=True) 
    no_column33 = models.CharField(max_length=20,null=True)
    dato_actual33 = models.CharField(max_length=255,null=True)
    dato_anteri33 = models.CharField(max_length=255,null=True) 
    no_column34 = models.CharField(max_length=20,null=True) 
    dato_actual34 = models.CharField(max_length=255,null=True) 
    dato_anteri34 = models.CharField(max_length=255,null=True) 
    no_column35 = models.CharField(max_length=20,null=True) 
    dato_actual35 = models.CharField(max_length=255,null=True)
    dato_anteri35 = models.CharField(max_length=255,null=True) 
    no_column36 = models.CharField(max_length=20,null=True)
    dato_actual36 = models.CharField(max_length=255,null=True) 
    dato_anteri36 = models.CharField(max_length=255,null=True) 
    no_column37 = models.CharField(max_length=20,null=True) 
    dato_actual37 = models.CharField(max_length=255,null=True) 
    dato_anteri37 = models.CharField(max_length=255,null=True) 
    no_column38 = models.CharField(max_length=20,null=True) 
    dato_actual38 = models.CharField(max_length=255,null=True) 
    dato_anteri38 = models.CharField(max_length=255,null=True)
    no_column39 = models.CharField(max_length=20,null=True)
    dato_actual39 = models.CharField(max_length=255,null=True) 
    dato_anteri39 = models.CharField(max_length=255,null=True) 
    no_column40 = models.CharField(max_length=20,null=True) 
    dato_actual40 = models.CharField(max_length=255,null=True) 
    dato_anteri40 = models.CharField(max_length=255,null=True) 
    no_column41 = models.CharField(max_length=20,null=True) 
    dato_actual41 = models.CharField(max_length=255,null=True)
    dato_anteri41 = models.CharField(max_length=255,null=True) 
    no_column42 = models.CharField(max_length=20,null=True)
    dato_actual42 = models.CharField(max_length=255,null=True) 
    dato_anteri42 = models.CharField(max_length=255,null=True)
    no_column43 = models.CharField(max_length=20,null=True) 
    dato_actual43 = models.CharField(max_length=255,null=True) 
    dato_anteri43 = models.CharField(max_length=255,null=True) 
    no_column44 = models.CharField(max_length=20,null=True) 
    dato_actual44 = models.CharField(max_length=255,null=True)
    dato_anteri44 = models.CharField(max_length=255,null=True) 
    no_column45 = models.CharField(max_length=20,null=True) 
    dato_actual45 = models.CharField(max_length=255,null=True) 
    dato_anteri45 = models.CharField(max_length=255,null=True) 
    no_column46 = models.CharField(max_length=20,null=True) 
    dato_actual46 = models.CharField(max_length=255,null=True)
    dato_anteri46 = models.CharField(max_length=255,null=True)
    no_column47 = models.CharField(max_length=20,null=True)
    dato_actual47 = models.CharField(max_length=255,null=True) 
    dato_anteri47 = models.CharField(max_length=255,null=True) 
    no_column48 = models.CharField(max_length=20,null=True) 
    dato_actual48 = models.CharField(max_length=255,null=True) 
    dato_anteri48 = models.CharField(max_length=255,null=True) 
    no_column49 = models.CharField(max_length=20,null=True)
    dato_actual49 = models.CharField(max_length=255,null=True) 
    dato_anteri49 = models.CharField(max_length=255,null=True) 
    no_column50 = models.CharField(max_length=20,null=True) 
    dato_actual50 = models.CharField(max_length=255,null=True) 
    dato_anteri50 = models.CharField(max_length=255,null=True)
    no_column51 = models.CharField(max_length=20,null=True)
    dato_actual51 = models.CharField(max_length=255,null=True) 
    dato_anteri51 = models.CharField(max_length=255,null=True) 
    no_column52 = models.CharField(max_length=20,null=True) 
    dato_actual52 = models.CharField(max_length=255,null=True)
    dato_anteri52 = models.CharField(max_length=255,null=True) 
    no_column53 = models.CharField(max_length=20,null=True)
    dato_actual53 = models.CharField(max_length=255,null=True)
    dato_anteri53 = models.CharField(max_length=255,null=True) 
    no_column54 = models.CharField(max_length=20,null=True)
    dato_actual54 = models.CharField(max_length=255,null=True) 
    dato_anteri54 = models.CharField(max_length=255,null=True) 
    no_column55 = models.CharField(max_length=20,null=True)
    dato_actual55 = models.CharField(max_length=255,null=True)
    dato_anteri55 = models.CharField(max_length=255,null=True) 
    no_column56 = models.CharField(max_length=20,null=True) 
    dato_actual56 = models.CharField(max_length=255,null=True) 
    dato_anteri56 = models.CharField(max_length=255,null=True)
    no_column57 = models.CharField(max_length=20,null=True)
    dato_actual57 = models.CharField(max_length=255,null=True)
    dato_anteri57 = models.CharField(max_length=255,null=True)
    no_column58 = models.CharField(max_length=20,null=True)
    dato_actual58 = models.CharField(max_length=255,null=True) 
    dato_anteri58 = models.CharField(max_length=255,null=True) 
    no_column59 = models.CharField(max_length=20,null=True) 
    dato_actual59 = models.CharField(max_length=255,null=True) 
    dato_anteri59 = models.CharField(max_length=255,null=True) 
    no_column60 = models.CharField(max_length=20,null=True) 
    dato_actual60 = models.CharField(max_length=255,null=True) 
    dato_anteri60 = models.CharField(max_length=255,null=True) 

    class Meta:
        db_table='segaud1'

class SegGxbo(models.Model):
    gerencia_apl = models.CharField(max_length=2) 
    tipo_articulo = models.CharField(max_length=2)
    gerencia_bodega = models.CharField(max_length=2)

    class Meta:
        db_table='seggxbo'


class SegUcon(models.Model):
    usuario = models.CharField(max_length=10)
    secuencia = models.SmallIntegerField()
    contrasena_ant = models.CharField(max_length=10)
    contrasena_act = models.CharField(max_length=10)
    fecha_cambio = models.DateField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segucon'

class Segfiscal(models.Model):
    impresora = models.CharField(max_length=3)
    fiscal = models.IntegerField()
    descripcion = models.CharField(max_length=30)
    mac_address = models.CharField(max_length=25,null=True) 
    puerto = models.CharField(max_length=10,null=True)
    no_registro = models.CharField(max_length=25,null=True)
    secuencial = models.IntegerField(null=True)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creacion = models.DateField(null=True)
    hora_creacion = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segfiscal'

class Seglogin(models.Model):
    usuario = models.CharField(max_length=10)
    no_sesion = models.IntegerField()
    compania = models.CharField(max_length=3,null=True)
    agencia = models.CharField(max_length=3,null=True)
    base_datos = models.CharField(max_length=18,null=True)
    fechalogin = models.DateTimeField(null=True)
    usuario_bd = models.CharField(max_length=10,null=True)
    contrasena_bd = models.CharField(max_length=10,null=True)

    class Meta:
        db_table='seglogin'

class Syslic(models.Model):
     no_licencia = models.IntegerField()

     class Meta:
         db_table='syslic'

class Segrgla(models.Model):
    tipo_clave = models.CharField(max_length=1)
    secuencia = models.SmallIntegerField(null=True)
    posicion = models.CharField(max_length=1,null=True) 
    caracter = models.CharField(max_length=1,null=True)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creado = models.DateField(null=True)
    hora_creado = models.DateTimeField(null=True)
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True)
    hora_status = models.DateTimeField(null=True)

    class Meta:
       db_table='segrgla'

class Segtcla(models.Model):
    tipo_clave = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=30,null=True)
    tamano = models.SmallIntegerField(null=True)
    creado_por = models.CharField(max_length=10,null=True)
    fecha_creado = models.DateField(null=True)
    hora_creado = models.DateTimeField(null=True) 
    modificado_por = models.CharField(max_length=10,null=True)
    fecha_status = models.DateField(null=True) 
    hora_status = models.DateTimeField(null=True)

    class Meta:
        db_table='segtcla'

class Segcpas(models.Model):
    usuario = models.CharField(max_length=10)
    politica = models.CharField(max_length=1)
    ciclo = models.SmallIntegerField(null=True)
    avisos = models.SmallIntegerField(null=True)
    repite_pass = models.CharField(max_length=1,null=True) 
    fecha_cambio = models.DateField(null=True)
    hora_cambio = models.DateTimeField(null=True)
    status = models.CharField(max_length=1,null=True)

    class Meta:
        db_table='segcpas'

class Seghpas(models.Model):
    usuario = models.CharField(max_length=10) 
    fecha_cambio = models.DateField() 
    hora_cambio = models.DateTimeField(null=True)
    pass_ant = models.CharField(max_length=8,null=True)
    pass_act = models.CharField(max_length=8,null=True)

    class Meta:
        db_table='seghpas'
