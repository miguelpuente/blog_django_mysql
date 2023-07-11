from . import models

# Acerca
def contexto_acerca(request):
    return {'acerca':models.Acerca.objects.latest('creacion')}


# Categorías
def contexto_categoria(request):
    return {'categorias':models.Categoria.objects.filter(activo=True)}


# Archivos
def contexto_historial(request):
    return {'dates':models.Articulo.objects.dates('creacion', 'month', order='DESC')}

# Redes Sociales
def contexto_link(request):
    return {'contexto':models.Link.objects.all()}