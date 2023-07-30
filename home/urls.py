from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.home, name = 'home-blog'),
    path('register/',views.register,name='register'),
    path('info/',views.infos,name='info-blog'),

]