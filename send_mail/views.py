from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from send_mail.models import Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'email', 'comment',)
    success_url = reverse_lazy('send_mail:list')


class ClientListView(ListView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('name', 'email', 'comment',)
    success_url = reverse_lazy('send_mail:list')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('send_mail:list')
