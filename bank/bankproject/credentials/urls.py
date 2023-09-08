from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('apply',views.apply,name='apply'),
    path('new',views.new,name='new'),
    path('done',views.done,name='done'),
]