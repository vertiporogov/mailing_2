from django import forms

from send_mail.models import Client, MailingModel, MailingMassage


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailingModelForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingModel
        fields = '__all__'


class MailingMassageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = MailingMassage
        fields = '__all__'
