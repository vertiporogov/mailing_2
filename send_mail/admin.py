# from django.contrib import admin
#
# from send_mail.models import Client, MailingMassage, MailingModel, MailingList
#
#
# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'name', 'email', 'comment',)
#     list_filter = ('email',)
#
#
# @admin.register(MailingMassage)
# class MailingMassageAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'name_massage', 'topic_massage', 'body_massage',)
#
#
# @admin.register(MailingModel)
# class MailingModelAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'name_mailing', 'start_time', 'end_time', 'send', 'is_activ', 'send_end',)
#     list_filter = ('name_mailing',)
#
#
# @admin.register(MailingList)
# class MailingListAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'client', 'name_mailing',)
