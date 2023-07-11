from django.contrib import admin
from . import models

admin.site.site_header = 'Administración del Blog'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Blog'


# Categoría
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')

admin.site.register(models.Categoria, CategoriaAdmin)


# Etiqueta
class EtiquetaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre', 'activo', 'creacion')

admin.site.register(models.Etiqueta, EtiquetaAdmin)


# Articulo
class ArticuloAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('titulo', 'categoria', 'publicado', 'autor' ,'creacion', 'articuloEtiquetas')
    ordering = ('autor', '-creacion')
    search_fields = ('titulo', 'contenido', 'autor__username', 'categoria__nombre')
    list_filter = ('autor', 'categoria', 'etiquetas')

    def articuloEtiquetas(self, obj):
        return ' - '.join([etiqueta.nombre for etiqueta in obj.etiquetas.all().order_by('nombre')])
    
    articuloEtiquetas.short_description = 'Etiquetas'

admin.site.register(models.Articulo, ArticuloAdmin)


# Acerca
class AcercaAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('descripcion','creacion')

admin.site.register(models.Acerca, AcercaAdmin)


# Redes Sociales

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('creacion', 'actualizacion')
    list_display = ('nombre','key', 'url', 'icono')

admin.site.register(models.Link, LinkAdmin)