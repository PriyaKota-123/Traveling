from django.urls import path
from.import views
urlpatterns=[
    path('5',views.home),
    path('1', views.sign_up, name='signup'),
    path('2/', views.user_login, name='login1'),
    path('3', views.user_logout, name='logout'),
    path('4/', views.profile,name='profile'),

]