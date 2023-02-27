from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import RegisterForm, PostForm
from django.views.generic import ListView, FormView, UpdateView, DeleteView, CreateView
from django.views.generic import DetailView


class NewsList(LoginRequiredMixin, ListView):
    login_url = 'news:login'
    template_name = 'news/list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10


class NewsCreate(LoginRequiredMixin, CreateView):
    login_url = 'news:login'
    template_name = 'news/post_create.html'
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('news:news_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsDetail(LoginRequiredMixin, DetailView):
    login_url = 'news:login'
    template_name = 'news/detail.html'
    model = Post


class NewsUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'news:login'
    template_name = 'news/post_update.html'
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('news:news_list')


class NewsDelete(LoginRequiredMixin, DeleteView):
    login_url = 'news:login'
    model = Post
    success_url = reverse_lazy('news:news_list')


class NewsLoginView(LoginView):
    template_name = 'registration/login.html'


class NewsLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Rejestracja zakończona pomyślnie.')
            return redirect('news:news_list')
        messages.error(request, 'Nieudana rejestracja. Nieprawidłowe informacje.')
        return render(request, 'registration/register.html', {'form': form})
