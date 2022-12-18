from django.urls import include, path

from .views import ProfileView, WhoamiView, TopFiveRankingView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/profile/', ProfileView.as_view()),
    path('auth/whoami/', WhoamiView.as_view()),
    path('top_five_ranking/', TopFiveRankingView.as_view()),
]
