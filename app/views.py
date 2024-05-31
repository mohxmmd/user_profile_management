from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import UserProfile, Portfolio, Project
from .forms import UserProfileForm, PortfolioForm, ProjectForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView



class UserProfileListView(ListView):
    model = UserProfile
    template_name = 'profile_list.html'
    context_object_name = 'profiles'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            profile = self.request.user.userprofile
        except UserProfile.DoesNotExist:
            profile = UserProfile(user=self.request.user)
            profile.save()
        context['form'] = UserProfileForm(instance=profile)
        return context

    def post(self, request, *args, **kwargs):
        try:
            profile = self.request.user.userprofile
        except UserProfile.DoesNotExist:
            profile = UserProfile(user=self.request.user)
            profile.save()
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})


class EditProfileView(ProfileView):
    template_name = 'edit_profile.html'


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio_detail.html'


class PortfolioView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            portfolio = self.request.user.portfolio
        except Portfolio.DoesNotExist:
            portfolio = Portfolio(user=self.request.user)
            portfolio.save()
        context['form'] = PortfolioForm(instance=portfolio)
        return context

    def post(self, request, *args, **kwargs):
        try:
            portfolio = self.request.user.portfolio
        except Portfolio.DoesNotExist:
            portfolio = Portfolio(user=self.request.user)
            portfolio.save()
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
        return render(request, self.template_name, {'form': form})


class EditPortfolioView(PortfolioView):
    template_name = 'edit_portfolio.html'


class AddProjectView(LoginRequiredMixin, CreateView):
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


class EditProjectView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'edit_project.html'

    def get_success_url(self):
        return reverse_lazy('portfolio')


class DeleteProjectView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('portfolio')

    def get_success_url(self):
        return reverse_lazy('portfolio')

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


