from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView

from send_mail.models import Client, MailingMassage, MailingModel, MailingList


class HomeView(TemplateView):
    template_name = 'send_mail/home.html'
    extra_context = {
        'title': 'Рассылки - Главная'
    }


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
    fields = ('name_mailing', 'start_time', 'end_time', 'body_massage', 'email')
    success_url = reverse_lazy('send_mail:list_mailingmodel')


class MailingModelListView(ListView):
    model = MailingModel


class MailingModelDetailView(DetailView):
    model = MailingModel


class MailingModelUpdateView(UpdateView):
    model = MailingModel
    fields = ('name_mailing', 'start_time', 'end_time', 'body_massage', 'email')
    success_url = reverse_lazy('send_mail:list_mailingmodel')


class MailingModelDeleteView(DeleteView):
    model = MailingModel
    success_url = reverse_lazy('send_mail:list_mailingmodel')


class MailingListCreateView(CreateView):
    model = MailingList
    fields = ('name_mailing', 'client',)
    success_url = reverse_lazy('send_mail:list_mailinglist')


class MailingListUpdateView(UpdateView):
    model = MailingList
    fields = ('name_mailing', 'client',)
    success_url = reverse_lazy('send_mail:list_mailinglist')


class MailingListListView(ListView):
    model = MailingList


class MailingListDetailView(DetailView):
    model = MailingList


class MailingListDeleteView(DeleteView):
    model = MailingList
    success_url = reverse_lazy('send_mail:list_mailinglist')
