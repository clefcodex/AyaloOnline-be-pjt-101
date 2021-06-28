"""ayaloconfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from ayaloapp.views import Signup


 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



from rest_framework.routers import DefaultRouter
from phone_verify.api import VerificationViewSet





schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
<<<<<<< HEAD
    path('signup/', Signup.as_view()),
    path('', include('authemail.urls')),
    path('api/', include('ayaloapp.urls'))
=======
    path('email-auth/signup/', Signup.as_view()),
    path('email-auth/', include('authemail.urls'))
>>>>>>> 5fae535ab9faf9a9b98ef1f242e69896ef63b07c
=======
    path('signup/', Signup.as_view()),
    path('', include('authemail.urls')),
    path('',include('productlisting_api.urls'))
    # path("", include('google_auth_api.urls'))
>>>>>>> 91dd32c46fc337f92001517e5da2bf5be7dbb913
]
