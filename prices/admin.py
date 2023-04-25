from django.contrib import admin

# Register your models here.
from .models import Download, Price, Symbol


class DownloadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Download, DownloadAdmin)
