from django.contrib import admin

# Register your models here.
from .models import Store, Good

admin.site.register(Store)
admin.site.register(Good)