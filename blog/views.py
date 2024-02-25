from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import MailingBlog


class MailingBlogListView(ListView):
    model = MailingBlog


class MailingBlogDetailView(DetailView):
    model = MailingBlog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save(update_fields=['views_count'])

        return self.object
