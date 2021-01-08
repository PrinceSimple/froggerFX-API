from rest_framework import routers
from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, UserList
from knox import views as knox_views

router = routers.DefaultRouter()
#router.register('api/', PlayerViewSet, 'froggerFX')
#router.register('api/v1/users', UserViewSet, 'froggerFX')

urlpatterns = [
  path('api/auth', include('knox.urls')),
  path('api/auth/register', RegisterAPI.as_view()),
  path('api/auth/login', LoginAPI.as_view()),
  path('api/user/<int:pk>/', UserAPI.as_view()),
  path('api/users', UserList.as_view()),
  path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]

urlpatterns += router.urls