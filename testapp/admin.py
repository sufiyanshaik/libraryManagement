from django.contrib import admin
from testapp.models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['Name','Author','Pages','Cost']
admin.site.register(Book,BookAdmin)
