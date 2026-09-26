from django.urls import path
from . import views

app_name = 'careers'

urlpatterns = [
    # Core pages
    path('', views.home, name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Careers
    path('careers/', views.career_list, name='career_list'),
    path('careers/<slug:slug>/', views.career_detail, name='career_detail'),

    # Schools & Courses
    path('schools/', views.school_list, name='school_list'),
    path('schools/<int:pk>/', views.school_detail, name='school_detail'),
    path('courses/', views.course_list, name='course_list'),
    path('careers/<int:career_id>/', views.career_detail, name='career_detail'),

    # Assessment Steps
    path('assessment/step-1/', views.assessment_step1, name='assessment_step1'),
    path('assessment/step-2/', views.assessment_step2, name='assessment_step2'),
    path('assessment/step-3/', views.assessment_step3, name='assessment_step3'),
    path('assessment/step-4/', views.assessment_step4, name='assessment_step4'),
    path('assessment/step-5/', views.assessment_step5, name='assessment_step5'),
    path('assessment/results/<int:assessment_id>/', views.assessment_result, name='assessment_results'),
]