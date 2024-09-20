from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car, Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm

# HTML-представления

# Список автомобилей 
class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'

# Детали автомобиля
class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'

# Создание автомобиля
class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['make', 'model', 'year', 'description']
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

# Обновление автомобиля
class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['make', 'model', 'year', 'description']
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car-list')

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

# Удаление автомобиля
class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('car-list')

    def get_queryset(self):
        return Car.objects.filter(owner=self.request.user)

# Добавление комментария
class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'cars/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.car = get_object_or_404(Car, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('car-detail', kwargs={'pk': self.kwargs['pk']})

# Регистрация пользователей
class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
