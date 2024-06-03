"""
URL configuration for user_profile_management project.

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
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from django.conf import settings

router = DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserProfileListView.as_view(), name='profile'),
    path('createprofile/', views.ProfileView.as_view(), name='createprofile'),
    path('createportfolio/<int:userprofile_id>/', views.CreatePortfolioView.as_view(), name='createportfolio'),
    path('createproject/<int:userprofile_id>/', views.CreateProjectView.as_view(), name='createproject'), 
   path('profile/<int:pk>/delete/', views.DeleteProfileView.as_view(), name='delete_profile'),
    path('profile/<int:pk>/edit/', views.EditProfileView.as_view(), name='edit_profile'),

    
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
   
     path('portfolio/<int:portfolio_id>/add_project/', views.AddProjectView.as_view(), name='add_project'),
   
    
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('portfolio/<int:pk>/', views.PortfolioDetailView.as_view(), name='profile_detail')

]+router.urls+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


