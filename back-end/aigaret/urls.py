"""aigaret URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import AuthRegister, ChangePasswordView, IdDuplicateCheckView
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),

    #simplejwt
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #jwt
    path("api/rest-auth/", include('rest_auth.urls')),
    # path("rest-auth/signup/", include('rest_auth.registration.urls')),
    path("api/rest-auth/signup/", AuthRegister.as_view()),
    
    path("api/changepassword/", ChangePasswordView.as_view()),
    path("api/idDuplicateCheck/", IdDuplicateCheckView.as_view()),
    
    # games
    path('api/games/', include('games.urls')),

    # mypages
    path('api/mypages/', include('mypages.urls')),
]
