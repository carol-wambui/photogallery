from django.contrib import admin
from .models import Category,Image,Location
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Category),
admin.site.register(Image),
admin.site.register(Location)