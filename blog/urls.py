from django.urls import path
from blog.views import MailingBlogListView, MailingBlogDetailView

from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('list_blog/', MailingBlogListView.as_view(), name='list_blog'),
    path('view_blog/<int:pk>', MailingBlogDetailView.as_view(), name='view_blog'),
]
