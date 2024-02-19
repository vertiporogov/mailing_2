from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView

from blog.models import MailingBlog
from send_mail.forms import ClientForm, MailingModelForm, MailingMassageForm
from send_mail.models import Client, MailingMassage, MailingModel, MailingList
from users.models import User


class HomeView(TemplateView):
    template_name = 'send_mail/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Рассылки - Главная'
        context['blog'] = MailingBlog.objects.order_by('?')[:3]
        context['count_all'] = MailingModel.objects.all().count()
        context['count_active'] = MailingModel.objects.filter(is_active=True).count()
        context['client'] = Client.objects.all().count()
        # context['email'] = User.objects.filter('')
        return context
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['body'] = MailingBlog.objects.all()[:3]
    #     return context_data


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('send_mail:list_client')


class ClientListView(ListView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('send_mail:list_client')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('send_mail:list_client')


class MailingMassageCreateView(LoginRequiredMixin, CreateView):
    model = MailingMassage
    form_class = MailingMassageForm
    success_url = reverse_lazy('send_mail:list_mailingmassage')


class MailingMassageListView(ListView):
    model = MailingMassage


class MailingMassageUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingMassage
    form_class = MailingMassageForm
    success_url = reverse_lazy('send_mail:list_mailingmassage')


class MailingMassageDetailView(DetailView):
    model = MailingMassage


class MailingMassageDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingMassage
    success_url = reverse_lazy('send_mail:list_mailingmassage')


class MailingModelCreateView(LoginRequiredMixin, CreateView):
    model = MailingModel
    form_class = MailingModelForm
    success_url = reverse_lazy('send_mail:list_mailingmodel')



class MailingModelListView(ListView):
    model = MailingModel

class MailingModelDetailView(DetailView):
    model = MailingModel


class MailingModelUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingModel
    form_class = MailingModelForm
    success_url = reverse_lazy('send_mail:list_mailingmodel')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MailingModelDeleteView(DeleteView):
    model = MailingModel
    success_url = reverse_lazy('send_mail:list_mailingmodel')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class MailingListCreateView(LoginRequiredMixin, CreateView):
    model = MailingList
    fields = ('name_mailing', 'client',)
    success_url = reverse_lazy('send_mail:list_mailinglist')


class MailingListUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingList
    fields = ('name_mailing', 'client',)
    success_url = reverse_lazy('send_mail:list_mailinglist')


class MailingListListView(ListView):
    model = MailingList


class MailingListDetailView(DetailView):
    model = MailingList


class MailingListDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingList
    success_url = reverse_lazy('send_mail:list_mailinglist')
