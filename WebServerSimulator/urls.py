"""
URL configuration for WebServerSimulator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from Simulator.views import FireViewSet, SensorViewSet

router = routers.SimpleRouter()
router.register('fire', FireViewSet, basename='fire')
router.register('sensor', SensorViewSet, basename='sensor')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("simulator/", include("Simulator.urls")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
