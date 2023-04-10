# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airline5074(models.Model):
    a_id = models.CharField(primary_key=True, max_length=10)
    a_name = models.CharField(max_length=25)
    a_palce = models.CharField(max_length=50, blank=True, null=True)
    ser_phone = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'airline5074'


class Flight5074(models.Model):
    f_id = models.CharField(primary_key=True, max_length=25)
    dep_station = models.CharField(max_length=25)
    dest_station = models.CharField(max_length=25)
    dep_time = models.DateTimeField()
    arr_time = models.DateTimeField()
    seat = models.IntegerField()
    a_id = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'flight5074'


class Passenger5074(models.Model):
    p_id = models.CharField(primary_key=True, max_length=50)
    p_name = models.CharField(max_length=10)
    p_sex = models.CharField(max_length=10, blank=True, null=True)
    p_nation = models.CharField(max_length=10, blank=True, null=True)
    p_idnumber = models.CharField(unique=True, max_length=50, blank=True, null=True)
    workplace = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'passenger5074'


class Pticket5074(models.Model):
    t_id = models.CharField(primary_key=True, max_length=25)
    p = models.ForeignKey(Passenger5074, models.DO_NOTHING, blank=True, null=True)
    f = models.ForeignKey(Flight5074, models.DO_NOTHING, blank=True, null=True)
    s_level = models.CharField(max_length=10, blank=True, null=True)
    s_no = models.CharField(max_length=10, blank=True, null=True)
    de_gate = models.CharField(max_length=10, blank=True, null=True)
    ttpye = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pticket5074'


class Seat5074(models.Model):
    f = models.ForeignKey(Flight5074, models.DO_NOTHING, primary_key=True)
    s_level = models.CharField(max_length=10)
    price = models.IntegerField()
    s_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'seat5074'
        unique_together = (('f', 's_level'),)


class Up5074(models.Model):
    u = models.ForeignKey('User5074', models.DO_NOTHING, primary_key=True)
    p = models.ForeignKey(Passenger5074, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'up5074'
        unique_together = (('u', 'p'),)


class User5074(models.Model):
    u_id = models.CharField(primary_key=True, max_length=50)
    purview = models.CharField(max_length=10)
    u_password = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'user5074'
