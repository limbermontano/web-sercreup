from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Area(models.Model):
    id_are = models.AutoField(primary_key=True)
    nombre_are=models.CharField(max_length=50, unique=True)
    estado_are=models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.campo_no_duplicado

    def save(self, *args, **kwargs):
        try:
            super(Area, self).save(*args, **kwargs)
        except ValidationError as e:
            # Puedes personalizar el mensaje de alerta según tus necesidades
            mensaje_alerta = f"No se pudo guardar el registro: {e}"
            print(mensaje_alerta)
            # También puedes lanzar una excepción personalizada o realizar otras acciones aquí

class Cargo(models.Model):
  id_carg = models.AutoField(primary_key=True)
  nombre_carg=models.CharField(max_length=50)
  estado_carg=models.PositiveIntegerField(default=1)

class Documento(models.Model):
  id_doc = models.AutoField(primary_key=True)
  nombre_doc=models.CharField(max_length=50)
  estado_doc=models.PositiveIntegerField(default=1)
  
class Estudio(models.Model):
  id_est = models.AutoField(primary_key=True)
  nombre_est=models.CharField(max_length=50)
  estado_est=models.PositiveIntegerField(default=1)

class Profesion(models.Model):
  id_prof = models.AutoField(primary_key=True)
  nombre_prof=models.CharField(max_length=50)
  estado_prof=models.PositiveIntegerField(default=1)

class Persona(models.Model):
  id_per = models.AutoField(primary_key=True)
  nombre_per=models.CharField(max_length=15,verbose_name='Nombre')
  apellidoP_per=models.CharField(max_length=15, default="S/n", verbose_name='ApellidoP')
  apellidoM_per=models.CharField(max_length=15, default="S/n",verbose_name='ApellidoM')
  telf_per=models.CharField(max_length=10,verbose_name='Telefono')
  sexo_per=models.CharField(max_length=20,verbose_name='Tipo de sexo')
  numDoc_per=models.CharField(max_length=15, default="S/n", verbose_name='Numero de documento')
  exteDoc_per=models.CharField(max_length=6,verbose_name='Extension de documento')
  lugarNac_per=models.CharField(max_length=50,verbose_name='Lugar de nacimiento')
  sangre_per=models.CharField(max_length=10,verbose_name='Tipo de sangre')
  estCivil_per=models.CharField(max_length=20,verbose_name='Estado civil')
  imagen_per=models.ImageField(upload_to='imagenesPer/', default="S/n", verbose_name='Imagen',null=True)
  direccion_per=models.CharField(max_length=100, default="S/n", verbose_name='Direccion')
  documento_per=models.ForeignKey(Documento, null=True, blank=True, on_delete=models.CASCADE)
  estado_per=models.PositiveIntegerField(default=1)

class Personal(models.Model):
  id_perl = models.AutoField(primary_key=True)
  hijos_perl =models.PositiveIntegerField(default=0)
  fechIngre_perl=models.CharField(max_length=10,verbose_name='Fecha de ingreso')
  fechNac_perl =models.CharField(max_length=10,verbose_name='Fecha de Nacimiento ')
  venDoc_perl =models.CharField(max_length=10,verbose_name='Fecha vencimiento de documento')
  licCond_perl=models.CharField(max_length=2,verbose_name='Licencia de conducir')
  tipoLic_perl=models.CharField(max_length=10, null=True, blank=True, verbose_name='Tipo de Licencia')
  fechVenlic_perl=models.CharField(max_length=10, null=True, blank=True, verbose_name='Fecha vencimiento de licencia')
  ctaBanc_perl=models.CharField(max_length=20, default="S/n", verbose_name='Cuenta Bancaria')
  nua_perl=models.CharField(max_length=20,default="S/n", verbose_name='Cuenta Nua')
  ctaAfp_perl=models.CharField(max_length=20,verbose_name='Cuenta Afp')
  aseg_perl=models.CharField(max_length=20,verbose_name='Cuenta asegurado')
  sueldo_perl=models.FloatField(default=0)
  persona_perl=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
  area_perl=models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)
  cargo_perl=models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.CASCADE)
  estudio_perl=models.ForeignKey(Estudio, null=True, blank=True, on_delete=models.CASCADE)
  profesion_perl=models.ForeignKey(Profesion, null=True, blank=True, on_delete=models.CASCADE)
  estado_perl=models.PositiveIntegerField(default=1)
  
class Parentesco(models.Model):
  id_par = models.AutoField(primary_key=True)
  nombre_par=models.CharField(max_length=20,verbose_name='Nombre')
  estado_par=models.PositiveIntegerField(default=1)

class Zona(models.Model):
  id_zon = models.AutoField(primary_key=True)
  nombre_zon=models.CharField(max_length=50)
  estado_zon=models.PositiveIntegerField(default=1) 

class Fiscal(models.Model):
  id_fis = models.AutoField(primary_key=True)
  nombre_fis=models.CharField(max_length=20,verbose_name='Nombre')
  apellidoP_fis=models.CharField(max_length=30,default="S/n",verbose_name='ApellidoP')
  estado_fis=models.PositiveIntegerField(default=1)
  zona_fis=models.ForeignKey(Zona, null=True, blank=True, on_delete=models.CASCADE)

class Proyecto(models.Model):
  id_proy = models.AutoField(primary_key=True)
  nombre_proy=models.CharField(max_length=20,verbose_name='Nombre')
  grafo_proy=models.CharField(max_length=20,default="S/n",verbose_name='Grafo')
  trafo_proy=models.CharField(max_length=20,default="S/n",verbose_name='Trafo')
  ubicacion_proy=models.CharField(max_length=100,default="S/n",verbose_name='Ubicacion')
  nota_proy=models.CharField(max_length=70,default="S/n",verbose_name='Nota')
  fechaRecep_proy=models.CharField(max_length=10,verbose_name='Fecha de registro')
  fechaDisen_proy=models.CharField(max_length=10,verbose_name='Fecha de diseño')
  fechaConst_proy=models.CharField(max_length=10,verbose_name='Fecha de construccion')
  estado_proy=models.PositiveIntegerField(default=1)
  fiscal_proy=models.ForeignKey(Fiscal, null=True, blank=True, on_delete=models.CASCADE)
  

class Asignacion(models.Model):
  id_asig = models.AutoField(primary_key=True)
  nota_asig=models.CharField(max_length=70,default="S/n",verbose_name='Nota')
  fechaIni_asig=models.CharField(max_length=10,verbose_name='Fecha inicio')
  fechaFin_asig=models.CharField(max_length=10,null=True,blank=True,verbose_name='Fecha fin')
  estado_asig=models.PositiveIntegerField(default=1)  
  proyecto_asig=models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)
  personal_asig=models.ForeignKey(Personal, null=True, blank=True, on_delete=models.CASCADE) 

class Familiar(models.Model):
  id_fam = models.AutoField(primary_key=True)
  nombre_fam=models.CharField(max_length=20,verbose_name='Nombre')
  apellidoP_fam=models.CharField(max_length=30,verbose_name='ApellidoP')
  telef_fam=models.CharField(max_length=10,verbose_name='Telefono')
  nota_fam=models.CharField(max_length=70,default="S/n",verbose_name='nota')
  estado_fam=models.PositiveIntegerField(default=1)
  parentesco_fam=models.ForeignKey(Parentesco, null=True, blank=True, on_delete=models.CASCADE)
  personal_fam=models.ForeignKey(Personal, null=True, blank=True, on_delete=models.CASCADE)

class Envio(models.Model):
  id_env =models.AutoField(primary_key=True) 
  nota_env=models.CharField(max_length=70, default='S/N' ,verbose_name='nota')
  fechaEnv_env=models.CharField(max_length=10,verbose_name='Fecha envio')
  cronograma_env=models.BooleanField(default=False, verbose_name='Cronograma')
  estacado_env=models.BooleanField(default=False, verbose_name='Hoja Estacado')
  plano_env=models.BooleanField(default=False, verbose_name='Plano')
  puntoPunto_env=models.BooleanField(default=False, verbose_name='Punto a punto')
  manoObra_env=models.BooleanField(default=False, verbose_name='Mano de obra')
  resplado_env=models.BooleanField(default=False, verbose_name='Respaldo')
  estado_env=models.PositiveIntegerField(default=1)
  proyecto_env=models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)

class Ordent(models.Model):
  id_ord =models.AutoField(primary_key=True) 
  nota_ord=models.CharField(max_length=70, default='S/N' ,verbose_name='Nota')
  numero_ord=models.CharField(max_length=12 ,verbose_name='Numero de orden')
  numeroCaj_ord=models.CharField(max_length=4 ,verbose_name='Numero de caja')
  estado_ord=models.PositiveIntegerField(default=1)
  proyecto_ord=models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)