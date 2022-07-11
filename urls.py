from django.urls import path
from .views import  ExportCoincsv

urlpatterns = [
    path('coins_csv/', ExportCoincsv, name ='coins_csv'),
]