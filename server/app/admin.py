from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from .models import Store, Good, Profile

admin.site.register(Profile)
admin.site.register(Store)
admin.site.register(Good)