from django.urls import path

from send_mail.apps import SendMailConfig
from send_mail.views import ClientCreateView, ClientListView, ClientUpdateView, ClientDetailView, ClientDeleteView

app_name = SendMailConfig.name

urlpatterns = [
    path('create/', ClientCreateView.as_view(), name='create'),
    path('', ClientListView.as_view(), name='list'),
    path('edit/<int:pk>', ClientUpdateView.as_view(), name='edit'),
    path('view/<int:pk>', ClientDetailView.as_view(), name='view'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='delete'),
]