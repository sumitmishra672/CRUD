from django.contrib import admin
from .models import CRUD
# Register your models here.
@admin.register(CRUD)
class crudAdmin(admin.ModelAdmin):
    list_display=['id','name','price','description']