from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Post)

class PostAdmin(admin.ModelAdmin):
    list_display = [ 'title','city','img','body','author']

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','name','email','city','profile_picture']

    
# admin.site.register(models.Country)
@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'description','post']
    ordering = ['name']