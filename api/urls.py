from django.urls import path
from .views import Api_View, CustomerDetailedView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('portfolio/', Api_View.as_view(), name='api_view'),
    path('portfolio/<int:pk>/', CustomerDetailedView.as_view(), name='detailed_view'),
    path('api-token-auth/', views.obtain_auth_token),
    path('token', TokenObtainPairView.as_view(), name='tokenview'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refreshview')
]
