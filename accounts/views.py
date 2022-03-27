from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
