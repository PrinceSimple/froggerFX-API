from froggerFX.models import Player
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer, PlayerSerializer

#Viewset
""" class PlayerViewSet(viewsets.ModelViewSet):
  queryset = Player.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = PlayerSerializer """

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = UserSerializer(queryset, many=True)

# Register API
class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

# Login API
class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    _, token = AuthToken.objects.create(user)
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token
    })

# Get User API
class UserAPI(mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              generics.GenericAPIView):
  queryset = User.objects.all()
  permission_classes = [
    permissions.IsAuthenticated,
  ]
  serializer_class = UserSerializer
  
  def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)
  """
  def get_object(self):
    return self.request.user
   def list(self, request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return Response(serializer.data) """

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
