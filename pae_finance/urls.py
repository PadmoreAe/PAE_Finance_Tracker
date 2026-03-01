"""
URL configuration for pae_finance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from expenses.views import TotalBalanceView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/balance/total/', TotalBalanceView.as_view(), name='total-balance'),

    path('api/', include('expenses.urls')), # This connects serializer API
    
    # The login endpoint (Username/Password -> Token)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # The refresh endpoint (Get a new access token)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include('expenses.urls')),
]
