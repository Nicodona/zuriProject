from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup, name='signup'),path('login/', views.login, name='login'),  path('success', views.success, name='success'),
    path('logout/', views.logout, name='logout'),
    path('reset_password/', views.reset_password, name='reset_password')
]