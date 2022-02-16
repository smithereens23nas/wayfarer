from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Post)

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'city', 'img', 'body', 'author']
    list_display = [ 'title','get_city','img','body','author']
    
    def get_city(self, obj):
        return "\n".join([c.city for c in obj.city.all()])

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id','name','email','city','profile_picture']

    
# admin.site.register(models.Country)
@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'description']
    ordering = ['name']