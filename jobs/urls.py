# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),                 # /jobs/ -> list all jobs
    path('<int:pk>/', views.job_detail, name='job_detail'),    # /jobs/1/ -> job detail
    path('create/', views.job_create, name='job_create'),     # /jobs/create/ -> employer creates job
    path('<int:pk>/edit/', views.job_edit, name='job_edit'),  # /jobs/1/edit/ -> edit job
    path('<int:pk>/apply/', views.job_apply, name='job_apply'), # /jobs/1/apply/ -> apply form
]
