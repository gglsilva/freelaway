from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="account/password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name="account/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm_view.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), name="password_reset_complete"),
]