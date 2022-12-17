from django.urls import include, path

from .views import ProfileView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/profile/', ProfileView.as_view()),
]
