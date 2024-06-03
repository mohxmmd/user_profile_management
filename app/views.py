from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import UserProfile, Portfolio, Project
from .forms import UserProfileForm, PortfolioForm, ProjectForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView



class UserProfileListView(ListView):
    model = UserProfile
    template_name = '1.profile_list.html'
    context_object_name = 'profiles'

class ProfileView(CreateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = '2.createprofile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # Save the form to get the UserProfile object
        user_profile = form.save()
        # Redirect to 'createportfolio' with the userprofile_id parameter
        return redirect('createportfolio', userprofile_id=user_profile.pk)

class CreatePortfolioView(CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = '4.createportfolio.html'

    def get_success_url(self):
        return reverse_lazy('createproject', kwargs={'userprofile_id': self.object.user_profile.id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user_profile = get_object_or_404(UserProfile, pk=self.kwargs['userprofile_id'])
        self.object.user_profile = user_profile
        self.object.save()
        return super().form_valid(form)
    
class CreateProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = '5.createproject.html'  # Use a separate template for creating projects
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        portfolio = Portfolio.objects.get(user_profile_id=self.kwargs['userprofile_id'])
        self.object.portfolio = portfolio  # Assign the portfolio directly to the project
        self.object.save()
        return super().form_valid(form)



class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_detail.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            portfolio = self.request.user.portfolio
        except Portfolio.DoesNotExist:
            # If the user doesn't have a portfolio, create one
            portfolio = Portfolio(user=self.request.user)
            portfolio.save()
        context['form'] = PortfolioForm(instance=portfolio)
        return context




class AddProjectView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project.html'

    def form_valid(self, form):
        portfolio = get_object_or_404(Portfolio, pk=self.kwargs['portfolio_id'])
        form.instance.portfolio = portfolio
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('portfolio')
    
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'





class DeleteProfileView(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('profile')  # Redirect to the profile page after deletion

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())

class EditProfileView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm  # Assuming you have a form for editing the profile
    template_name = 'edit_profile.html'  # Your edit profile template
    success_url = reverse_lazy('profile')  # Redirect to the profile page after editing