
from django.contrib import admin
from django.urls import path, include
from card_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('card_list.urls'))
]
