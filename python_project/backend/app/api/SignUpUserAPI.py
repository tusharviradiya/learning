from app.models import AppUser
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework import permissions
from app.serializers.AppUserSerializer import AppUserSerializer


class SignUpUserAPI(APIView):
    permission_classes = [permissions.AllowAny]
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(AppUserSerializer(user).data)
