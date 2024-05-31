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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/profile/', views.UserProfileListView.as_view(), name='profile'),
    path('accounts/editprofile/', views.ProfileView.as_view(), name='editprofile'),    
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio/edit/', views.EditPortfolioView.as_view(), name='edit_portfolio'),
     path('portfolio/<int:portfolio_id>/add_project/', views.AddProjectView.as_view(), name='add_project'),
    path('portfolio/<int:project_id>/edit_project/', views.EditProjectView.as_view(), name='edit_project'),
    path('portfolio/<int:project_id>/delete_project/', views.DeleteProjectView.as_view(), name='delete_project'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('portfolio/<int:pk>/', views.PortfolioDetailView.as_view(), name='profile_detail')

]


