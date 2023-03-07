from django.db import models

# Create your models here.

class Resultados(models.Model):
    id_loteria=models.IntegerField()
    no_animal=models.CharField(max_length=2)
    fecha_lot=models.DateField()
    hr_gen_nu=models.TimeField()
    serv_gen=models.CharField(max_length=10)
    loteria=models.CharField(max_length=10)
        
class Administra(models.Model):
    dias_free=models.IntegerField()
    mon_tope=models.IntegerField()
    msg_global=models.CharField(max_length=100)
    status_adm=models.IntegerField()
   
class Tbl_registro(models.Model):
    nom_emp=models.CharField(max_length=20)
    nom_pro=models.CharField(max_length=20)
    ape_pro=models.CharField(max_length=20)
    tlf_pro=models.IntegerField()
    cor_pro=models.EmailField()
    fec_reg=models.DateField()
    fec_venc=models.DateField()
    blq=models.IntegerField()
    	
    