from django.urls import path

from .views import register_view, login_view, token_view

# from .views import Login, register_view, AnotherLogoutView

urlpatterns = [
    path('reg', register_view, name='reg'),
    path('login', login_view, name='login'),
    path('token', token_view, name='token'),
]