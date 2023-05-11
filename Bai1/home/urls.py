from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index),
    path('information/', views.information),
    path('project/', views.projects),
    path('contact/', views.contact),
    path('register/', views.register, name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
]