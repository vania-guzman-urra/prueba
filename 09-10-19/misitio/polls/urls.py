from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # ex: /encuestas/2/
    path('<int:id_pregunta>/', views.detalle, name='detalle'),

    # ex: /encuestas/5/resultados/
    path('<int:total>/resultados/', views.resultados, name='resultados'),
]