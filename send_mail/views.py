from django.shortcuts import render
from django.views.generic import CreateView

from send_mail.models import Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'email', 'comment',)

    def form_valid(self, form):
        pass
