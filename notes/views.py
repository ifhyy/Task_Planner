from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *


class NotesListView(ListView):
    model = Note

    def get_queryset(self):
        try:
            return Note.objects.filter(owner=self.request.user, active=True)
        except TypeError:
            return None

class NotesDetailView(DetailView):
    model = Note

    def get_queryset(self):
        return reverse('notes:note-detail')


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'notes/register.html'
    success_url = reverse_lazy('notes:note_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('notes:note_list')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'notes/login.html'
    success_url = reverse_lazy('notes:note_list')

    def get_success_url(self):
        return reverse_lazy('notes:note_list')


def logout_user(request):
    logout(request)
    return redirect('notes:login')
