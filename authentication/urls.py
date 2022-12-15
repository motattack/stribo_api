from django.urls import path

from .views import LoginView, TokenView, RegisterView

urlpatterns = [
    path('reg/', RegisterView.as_view(), name='reg'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', TokenView.as_view(), name='token'),
]
