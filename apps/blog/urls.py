from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('post/<int:articulo_id>', views.post, name= 'post'),
    path('author/<int:autor_id>', views.author, name= 'author'),
    path('category/<int:categoria_id>', views.category, name= 'category'),
    path('dates/<int:month_id>/<int:year_id>', views.dates, name= 'dates'),
]