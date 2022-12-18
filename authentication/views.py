from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, UserRankingSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class WhoamiView(APIView):
    def get(self, request):
        print(request.body)
        return Response(request.body)

    def post(self, request):
        print(request.body)
        return Response(request.body)


class TopFiveRankingView(APIView):
    def get(self, request):
        queryset = User.objects.all().order_by('-level')[:5]
        serializer = UserRankingSerializer(queryset, many=True)
        return Response(serializer.data)
