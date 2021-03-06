from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup' ),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('mypage/', views.mypage, name='mypage'),
    path('userInfoChange/',views.userInfoChange, name='userInfoChange'),
    path('passwordChange/',views.passwordChange, name='passwordChange'),
]