from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('selected/', views.selected_candidates, name='selected_candidates'),
    path('rejected/', views.rejected_candidates, name='rejected_candidates'),
]
