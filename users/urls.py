from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('reg/', views.reg, name='reg'),
    path('logout/', views.logout, name='logout'),
    path('users-cart/', views.users_cart, name='users_cart')
    

]