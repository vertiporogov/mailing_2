from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from send_mail.models import Client, MailingMassage, MailingModel


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'email', 'comment',)
    success_url = reverse_lazy('send_mail:list_client')


class ClientListView(ListView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('name', 'email', 'comment',)
    success_url = reverse_lazy('send_mail:list_client')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('send_mail:list_client')


class MailingMassageCreateView(CreateView):
    model = MailingMassage
    fields = ('name_massage', 'topic_massage', 'body_massage',)
    success_url = reverse_lazy('send_mail:list_mailingmassage')


class MailingMassageListView(ListView):
    model = MailingMassage


class MailingMassageUpdateView(UpdateView):
    model = MailingMassage
    fields = ('name_massage', 'topic_massage', 'body_massage',)
    success_url = reverse_lazy('send_mail:list_mailingmassage')


class MailingMassageDetailView(DetailView):
    model = MailingMassage


class MailingMassageDeleteView(DeleteView):
    model = MailingMassage
    success_url = reverse_lazy('send_mail:list_mailingmassage')


class MailingModelCreateView(CreateView):
    model = MailingModel
    fields = ('name_mailing', 'start_time', 'end_time', 'body_massage')
    success_url = reverse_lazy('send_mail:list_mailingmodel')


class MailingModelListView(ListView):
    model = MailingModel


class MailingModelDetailView(DetailView):
    model = MailingModel


class MailingModelUpdateView(UpdateView):
    model = MailingModel
    fields = ('name_mailing', 'start_time', 'end_time', 'body_massage')
    success_url = reverse_lazy('send_mail:list_mailingmodel')


class MailingModelDeleteView(DeleteView):
    model = MailingModel
    success_url = reverse_lazy('send_mail:list_mailingmodel')

