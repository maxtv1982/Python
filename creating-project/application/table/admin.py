from django.contrib import admin

from django.contrib import admin
from table.models import Table, File


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
       pass

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
       pass

