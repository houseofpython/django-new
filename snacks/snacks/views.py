from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.shortcuts import render
from django.urls import reverse_lazy


class SnackListView(ListView):
    template_name = 'snack-list.html'
    model = Snack
    content_object_name = 'snack_tracker'


class SnackDetailView(DetailView):
    template_name = 'snack-detail.html'
    model = Snack


# Create your views here.
class SnackCreateView(CreateView):
    template_name = 'snack-create.html'
    model = Snack
    fields = ['name', 'description', 'purchaser']


class SnackUpdateView(UpdateView):
    template_name = 'snack-update.html'
    model = Snack
    fields = ['name', 'description', 'purchaser']


class SnackDeleteView(DeleteView):
    template_name = 'snack-delete.html'
    model = Snack
    success_url = reverse_lazy('snack-list')

