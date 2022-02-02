from django import forms
from django.core import validators


class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام و نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(120, 'نام و نام خانوادگی شما نباید بیشتر از 150 کاراکتر باشد')
        ]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید', 'class': 'form-control'}),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(100, 'ایمیل شما نباید بیشتر از 150 کاراکتر باشد')
        ]
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا موضوع پیام را وارد نمایید', 'class': 'form-control'}),
        label='موضوع پیام',
        validators=[
            validators.MaxLengthValidator(200, 'موضوع پیام شما نباید بیشتر از 150 کاراکتر باشد')
        ]
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا متن پیام خود را وارد نمایید', 'class': 'form-control', 'id': 'message'}),
        label='متن پیام'
    )
