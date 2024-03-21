from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Realtor
# Register your models here.
@admin.register(Realtor)
class ListingAdmin(admin.ModelAdmin):
    list_display=['id','name','email','is_mvp']
    list_display_links=['id','name']
    list_editable=['is_mvp']

    search_fields=['name']
    list_per_page=25

    
