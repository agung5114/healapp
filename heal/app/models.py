# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pasien(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    umur = models.IntegerField()
    bb = models.IntegerField()
    tb = models.IntegerField()
    gender = models.CharField(max_length=20)
    penyakit = models.CharField(max_length=40)
    diabetes = models.BooleanField()
    jantung = models.BooleanField()
    
class Makanan(models.Model):
    menu = models.CharField(max_length=128, primary_key=True)
    kkal = models.IntegerField()
    lemak = models.IntegerField()
    karbohidrat = models.IntegerField()
    protein = models.IntegerField()
    risiko = models.CharField(max_length=64)
    
class Makan(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_makan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
class Minum(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_minum = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    
class Userdata(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=128)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    umur = models.IntegerField()
    bb = models.IntegerField()
    tb = models.IntegerField()
    gender = models.CharField(max_length=20)
    penyakit = models.CharField(max_length=40)
    diabetes = models.BooleanField()
    jantung = models.BooleanField()