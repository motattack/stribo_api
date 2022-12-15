from rest_framework.routers import DefaultRouter

from .views import CommentViewSet

r = DefaultRouter()
r.register('comment', CommentViewSet)

urlpatterns = [
] + r.urls
