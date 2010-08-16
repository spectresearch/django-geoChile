from django.contrib.gis.db import models

class Region(models.Model):
    '''
    A region
    '''
    id = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.nombre
    
class Provincia(models.Model):
    '''
    A province
    '''
    id = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region)
    
    def __unicode__(self):
        return self.nombre

class Comuna(models.Model):
    '''
    A town, municipality
    '''
    nombre = models.CharField(max_length=30)
    ubicacion = models.PointField(srid=4326)
    provincia = models.ForeignKey(Provincia)
    region = models.ForeignKey(Region)
    objects = models.GeoManager()  
    
    class Meta:
        ordering = ('nombre',)
        
    def __unicode__(self):
        return self.nombre
