"""
URL configuration for scholarpg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #student urls
    path('', views.homepage), #Home/Dashboard
    path('view_student/<int:pk>', views.view_student),# view 1 student by id
    path('add_student_form/', views.add_student_form),#form to add a student
    path('add_student/', views.add_student), #submit form to add a student
    path('update_student_form/<int:pk>', views.update_student_form),
    path('update_student/<int:pk>', views.update_student, name='update'),
    path('delete_student_form/<int:pk>', views.delete_student_form),
    path('delete_student/<int:pk>', views.delete_student, name='delete'),
    #behavior urls
    path('view_behaviors/', views.view_behaviors),
    path('add_behavior_form/', views.add_behavior_form),
    path('add_behavior/', views.add_behavior),
    path('update_behavior_form/<int:pk>', views.update_behavior_form),
    path('update_behavior/<int:pk>', views.update_behavior, name='update'),
    path('delete_behavior_form/<int:pk>', views.delete_behavior_form),
    path('delete_behavior/<int:pk>', views.delete_behavior, name='delete'),
    path('award_behavior/', views.award_behavior),
    #skills urls
    path('view_skills/', views.view_skills),
    path('add_skill_form/', views.add_skill_form),
    path('add_skill/', views.add_skill),
    path('update_skill_form/<int:pk>', views.update_skill_form),
    path('update_skill/<int:pk>', views.update_skill, name='update'),
    path('delete_skill_form/<int:pk>', views.delete_skill_form),
    path('delete_skill/<int:pk>', views.delete_skill, name='delete'),
    path('use_skill/', views.use_skill),
#classroom tools
    #random event urls
    path('classroom_tools/', views.view_classroom_tools),
    path('view_random_event/', views.view_random_event),
    path('view_random_events/', views.view_random_events),
    path('add_random_event_form/', views.add_random_event_form),
    path('add_random_event/', views.add_random_event),
    path('update_random_event_form/<int:pk>', views.update_random_event_form),
    path('update_random_event/<int:pk>', views.update_random_event, name='update'),
    path('delete_random_event_form/<int:pk>', views.delete_random_event_form),
    path('delete_random_event/<int:pk>', views.delete_random_event, name='delete'),
    #miracle urls
    path('classroom_tools/', views.view_classroom_tools),
    path('view_miracle/', views.view_miracle),
    path('view_miracles/', views.view_miracles),
    path('add_miracle_form/', views.add_miracle_form),
    path('add_miracle/', views.add_miracle),
    path('update_miracle_form/<int:pk>', views.update_miracle_form),
    path('update_miracle/<int:pk>', views.update_miracle, name='update'),
    path('delete_miracle_form/<int:pk>', views.delete_miracle_form),
    path('delete_miracle/<int:pk>', views.delete_miracle, name='delete'),
    
]
