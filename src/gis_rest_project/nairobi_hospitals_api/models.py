from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class NairobiCounty(models.Model):
    geom = models.PolygonField(blank=True, null=True)
    objectid = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    perimeter = models.FloatField(blank=True, null=True)
    county3_field = models.FloatField(db_column='county3_', blank=True, null=True)  # Field renamed because it ended with '_'.
    county3_id = models.FloatField(blank=True, null=True)
    county = models.CharField(max_length=20, blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    number_2009_popul = models.CharField(db_column='2009_popul', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    pop = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nairobi_county'


class NairobiHealthFacilities(models.Model):
    geom = models.PointField(blank=True, null=True)
    addr_city = models.CharField(db_column='addr:city', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_street = models.CharField(db_column='addr:street', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(db_column='contact:phone', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'nairobi_health_facilities'


class NairobiSubCounties(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    constituen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nairobi_sub_counties'


class PointcloudFormats(models.Model):
    pcid = models.IntegerField(primary_key=True)
    srid = models.IntegerField(blank=True, null=True)
    schema = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pointcloud_formats'
