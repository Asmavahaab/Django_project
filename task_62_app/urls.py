from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('', views.login_user,name='login'),
    path('logout/', views.logOut, name='logout'),
    path('home/', views.home_page, name='home'),
    path('skill/', views.add_skills,name='add_skill'),
    path('update_skill/<int:skill_id>', views.update_skills, name='update_skill'),
    path('update_user/',views.update_user,name='update_user'),
    path('update_user_password/', views.update_user_password, name='update_user_password'),
    path('add_profile_details/', views.add_basic_details, name='add_user_details'),
    path('add_contact_details/',views.add_contact_details,name='add_contact_details'),
    path('portfolio/',views.portfolio_page,name='portfolio'),
    path('project/', views.project_page, name='project'),
    path('add_project_showcase/',views.project_showcase_create_view,name='project_add'),
    path('project_edit/<int:project_id>/',views.project_showcase_update_view,name='project_edit'),
    path('project_delete/<int:project_id>/',views.project_showcase_delete_view,name='project_delete'),
    path('add_work_experience/', views.add_work_experience, name='add_work'),
    path('edit_work_experience/<int:work_id>/', views.update_work_experience, name='edit_work'),
    path('delete_work_experience/<int:work_id>/', views.delete_work_experience, name='delete_work'),
    path('add_education/', views.add_education, name='add_education'),
    path('edit_education/<int:ed_id>/', views.update_education, name='edit_education'),
    path('delete_education/<int:ed_id>/', views.delete_education, name='delete_education'),
    path('add_certification/', views.add_certifications, name='add_certification'),
    path('edit_certification/<int:certificate_id>/', views.update_certifications, name='edit_certification'),
    path('delete_certification/<int:certificate_id>/', views.delete_certifications, name='delete_certification'),
    path('delete-account/', views.delete_account, name='delete_account'),

]