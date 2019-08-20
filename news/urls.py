from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('login/', views.AuthLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="login"),
    path('forget/', views.ForgetPasswordView.as_view(), name="forget"),
    path('success/', views.SuccessView.as_view(), name="success"),
    path('verify/<str:token>/<int:user_id>/', views.VerifyView.as_view(), name="verify"),
]
