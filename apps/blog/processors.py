from django.db.models.functions import ExtractMonth 
from . import models

# Acerca
def contexto_base(request):

    contexto = dict()

    # Acerca de

    if models.Acerca.objects.count():
        contexto['acerca'] = models.Acerca.objects.latest('creacion')
    else:
        contexto['acerca'] = ''
    
    # Categorias
    contexto['categorias'] = models.Categoria.objects.filter(activo=True)

    # Archivos
    # contexto['archivos'] = models.Articulo.objects.dates('creacion', 'month', order='DESC')

    meses = {
    1: 'enero',
    2: 'febrero',
    3: 'marzo',
    4: 'abril',
    5: 'mayo',
    6: 'junio',
    7: 'julio',
    8: 'agosto',
    9: 'septiembre',
    10: 'octubre',
    11: 'noviembre',
    12: 'diciembre'
    }

    contexto['archivos'] = [{'mes_letra':meses[fecha.month], 'fecha':fecha} for fecha in models.Articulo.objects.dates('creacion', 'month', order='DESC')]


    # Redes
    contexto['redes'] = models.Link.objects.all()


    return contexto