from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, TemplateView

from blog.models import MailingBlog
from send_mail.forms import ClientForm, MailingModelForm, MailingMassageForm
from send_mail.models import Client, MailingMassage, MailingModel, MailingList


class HomeView(TemplateView):
    template_name = 'send_mail/home.html'
    extra_context = {
        'title': 'Рассылки - Главная',
        'blog': MailingBlog.objects.all()[:3],
        'count_all': MailingModel.objects.all().count(),
        # 'count_active': MailingModel.objects.is_active().count(),
        'client': Client.objects.all().count(),
    }

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['body'] = MailingBlog.objects.all()[:3]
    #     return context_data

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('send_mail:list_client')


class ClientListView(ListView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('send_mail:list_client')


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('send_mail:list_client')


class MailingMassageCreateView(CreateView):
    model = MailingMassage
    form_class = MailingMassageForm
    success_url = reverse_lazy('send_mail:list_mailingmassage')


class MailingMassageListView(ListView):
    model = MailingMassage


class MailingMassageUpdateView(UpdateView):
    model = MailingMassage
    form_class = MailingMassageForm
    success_url = reverse_lazy('send_mail:list_mailingmassage')


class MailingMassageDetailView(DetailView):
    model = MailingMassage


class MailingMassageDeleteView(DeleteView):
    model = MailingMassage
    success_url = reverse_lazy('send_mail:list_mailingmassage')


class MailingModelCreateView(CreateView):
    model = MailingModel
    form_class = MailingModelForm
    success_url = reverse_lazy('send_mail:list_mailingmodel')

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #
    #     if self.object.owner != self.request.user:
    #         raise Http404
    #     return self.object


class MailingModelListView(ListView):
    model = MailingModel

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #
    #     if self.object.owner != self.request.user:
    #         raise Http404
    #     return self.object


class MailingModelDetailView(DetailView):
    model = MailingModel

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #
    #     if self.object.owner != self.request.user:
    #         raise Http404
    #     return self.object


class MailingModelUpdateView(UpdateView):
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
