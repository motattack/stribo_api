from rest_framework.viewsets import ModelViewSet

from .models import Comment
from .permissions import IsOwnerOrReadOnly
from .serizalizers import CommentSerializer


# Create your views here.
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
