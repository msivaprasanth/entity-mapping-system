"""
URL configuration for entity_mapping_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin # type: ignore
from django.urls import include, path # type: ignore
from rest_framework import permissions  # type: ignore
from drf_yasg.views import get_schema_view  # type: ignore
from drf_yasg import openapi  # type: ignore
from django.shortcuts import redirect  # type: ignore


schema_view = get_schema_view( 
    openapi.Info(
        title = "Entity Mapping System API",
        default_version = 'v1',
        description = "Manual API for Vendor , Product , Course and Certifications mappings",
        contact = openapi.Contact(email='contact@example.com'),
        license = openapi.License(name='BSD License'),
    ),
    public = True,
    permission_classes = (permissions.AllowAny,)
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', lambda request: redirect('/swagger/')),
    path('api/vendors/',include('vendor.urls')),
    path('api/products/',include('product.urls')),
    path('api/courses/',include('course.urls')),
    path('api/certifications/',include('certification.urls')),
    path('api/vendor-product-mappings/',include('vendor_product_mapping.urls')),
    path('api/product-course-mappings/',include('product_course_mapping.urls')),
    path('api/course-certification-mappings/',include('course_certification_mapping.urls')),

    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),
]
