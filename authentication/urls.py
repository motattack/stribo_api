from django.urls import include, path

from .views import ProfileView, WhoamiView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/profile/', ProfileView.as_view()),
    path('auth/whoami/', WhoamiView.as_view()),
]
