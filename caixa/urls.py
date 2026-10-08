from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('excluir/<int:gasto_id>/', views.excluir_gasto, name='excluir_gasto')
]
