from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('',views.main,name='main'),
    path('indexs/',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('update/', views.update, name='update'),
    path('<int:account_pk>/profile/',views.profile,name='profile'),
    path('<int:account_pk>/follow/',views.follow,name='follow'),
    path('password/', views.password_change, name='password_change'),
]
