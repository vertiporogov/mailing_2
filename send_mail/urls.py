from django.urls import path

from send_mail.apps import SendMailConfig

from send_mail.views import ClientCreateView, ClientListView, ClientUpdateView, ClientDetailView, ClientDeleteView, \
    MailingMassageCreateView, MailingMassageListView, MailingMassageUpdateView, MailingMassageDetailView, \
    MailingMassageDeleteView, MailingModelCreateView, MailingModelListView, MailingModelUpdateView, \
    MailingModelDetailView, MailingModelDeleteView, HomeView, MailingListCreateView, MailingListListView, \
    MailingListUpdateView, MailingListDeleteView, MailingListDetailView

app_name = SendMailConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('list_client/', ClientListView.as_view(), name='list_client'),
    path('edit_client/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('view_client/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    path('create_mailingmassage/', MailingMassageCreateView.as_view(), name='create_mailingmassage'),
    path('list_mailingmassage/', MailingMassageListView.as_view(), name='list_mailingmassage'),
    path('edit_mailingmassage/<int:pk>', MailingMassageUpdateView.as_view(), name='edit_mailingmassage'),
    path('view_mailingmassage/<int:pk>', MailingMassageDetailView.as_view(), name='view_mailingmassage'),
    path('delete_mailingmassage/<int:pk>', MailingMassageDeleteView.as_view(), name='delete_mailingmassage'),

    path('create_mailingmodel/', MailingModelCreateView.as_view(), name='create_mailingmodel'),
    path('list_mailingmodel/', MailingModelListView.as_view(), name='list_mailingmodel'),
    path('edit_mailingmodel/<int:pk>', MailingModelUpdateView.as_view(), name='edit_mailingmodel'),
    path('view_mailingmodel/<int:pk>', MailingModelDetailView.as_view(), name='view_mailingmodel'),
    path('delete_mailingmodel/<int:pk>', MailingModelDeleteView.as_view(), name='delete_mailingmodel'),

    path('create_mailinglist/', MailingListCreateView.as_view(), name='create_mailinglist'),
    path('list_mailinglist/', MailingListListView.as_view(), name='list_mailinglist'),
    path('edit_mailinglist/', MailingListUpdateView.as_view(), name='edit_mailinglist'),
    path('view_mailinglist/', MailingListDetailView.as_view(), name='view_mailinglist'),
    path('delete_mailinglist/', MailingListDeleteView.as_view(), name='delete_mailinglist'),
]
