from django.urls import path
# from.views import home
from . import views
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView,EditProfilePageView,AddProfilePageView,UserLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register'),
    # path('login/',UserLoginView, name='login'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(),name='change_password'),
    path('password-success/', views.password_success, name='password_success'),
    path('<int:pk>/profile',ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('addprofile/', AddProfilePageView.as_view(), name='add_Profile'),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
     name="reset_password"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_complete'),
]
