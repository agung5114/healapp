# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import Pasien, Makan, Minum, Makanan, Userdata
from django.contrib import admin
# from django import forms
# from django.forms import widgets

admin.site.register( Pasien )
admin.site.register( Makan )
admin.site.register( Minum )
admin.site.register( Makanan )
admin.site.register( Userdata )