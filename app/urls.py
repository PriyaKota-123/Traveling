from django.urls import path
from.import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('signup/', views.User_SignUp, name='signup'),
    path('login/', views.User_Login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('profile/', views.profile,name='profile'),
    path('about/',views.About,name='about'),

]