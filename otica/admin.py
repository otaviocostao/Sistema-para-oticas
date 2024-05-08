from django.contrib import admin

# Register your models here.

from core.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'endereco', 'data_nasc')

admin.site.register(Cliente, ClienteAdmin)