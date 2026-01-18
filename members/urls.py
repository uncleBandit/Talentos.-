# members/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # member dashboard
    path('profile/', views.profile, name='profile'),
    path('organizations/', views.organization_list, name='organization_list'),
    path('organizations/<int:pk>/', views.organization_detail, name='organization_detail'),
    path('membership/add/', views.add_membership, name='add_membership'),
]
