from django.urls import path
from . import views

app_name = 'kapital_bank'

urlpatterns = [
    # Template URL-ləri
    path('', views.kapital_list, name='kapital_list'),
    path('create/', views.kapital_create, name='kapital_create'),
    path('<int:pk>/', views.kapital_detail, name='kapital_detail'),
    path('<int:pk>/update/', views.kapital_update, name='kapital_update'),
    path('<int:pk>/delete/', views.kapital_delete, name='kapital_delete'),

    # API URL-ləri
    path('api/kapitals/', views.KapitalBankListCreateAPIView.as_view(), name='api_kapital_list_create'),
    path('api/kapitals/<int:pk>/', views.KapitalBankDetailAPIView.as_view(), name='api_kapital_detail'),
]
