
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<card_id>', views.delete, name='delete'),
    path('received/<card_id>', views.received, name='received'),
    path('not_received/<card_id>', views.not_received, name='not_received'),
    path('edit/<card_id>', views.edit, name='edit'),
]
