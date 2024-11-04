from django.urls import path
from .views import *

urlpatterns = [
    path('cars/', CarsListView.as_view(), name='cars_view'),
    path('sell/', SellCreateView.as_view(), name='sell_view'),
    path('car/<int:pk>', CarDetailView.as_view(), name='car_detail_view'),
    path('car/<int:pk>/update', CarUpdateView.as_view(), name='update_car'),
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='delete_car')
]