from django.contrib import admin

# Register your models here.
from .models import Dept,Hospital
admin.site.register(Dept)
admin.site.register(Hospital)