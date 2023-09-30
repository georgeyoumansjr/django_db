from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_mock_data, name='add_mock_data'),
    path('display/', views.display_mock_data, name='display_mock_data'),
]
