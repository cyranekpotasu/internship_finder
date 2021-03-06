"""internship_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from internship_finder.tags.views import TagViewSet
from .accounts.views import UserViewSet, StudentRegistrationAPIView
from .announcements.views import AnnouncementViewSet, ApplicationViewSet
from .companies.views import CompanyViewSet, OfficeViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='companies')
router.register(r'announcements', AnnouncementViewSet, basename='announcements')
router.register(r'users', UserViewSet, basename='users')
router.register(r'tags', TagViewSet, basename='tags')

companies_router = NestedSimpleRouter(router, r'companies', lookup='company')
companies_router.register(r'offices', OfficeViewSet, basename='company-offices')

announcements_router = NestedSimpleRouter(router, r'announcements', lookup='announcement')
announcements_router.register(r'applications', ApplicationViewSet, basename='announcement-applications')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(companies_router.urls)),
    path('api/', include(announcements_router.urls)),
    path('api/auth/', include('internship_finder.accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
