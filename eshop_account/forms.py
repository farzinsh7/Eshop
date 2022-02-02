from django import forms
from django.contrib.auth.models import User
from django.core import validators


class EditUserForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد نمایید', 'class': 'form-control'}),
        label='نام',
        validators=[
            validators.MaxLengthValidator(120, 'نام شما نباید بیشتر از 150 کاراکتر باشد')
        ]
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید', 'class': 'form-control'}),
        label='نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(120, 'نام خانوادگی شما نباید بیشتر از 150 کاراکتر باشد')
        ]
    )


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید'}),
        label='رمز ورود'
    )

    # def clean_user_name(self):
    #     user_name = self.cleaned_data.get('user_name')
    #     is_exists_user = User.objects.filter(username=user_name).exists()
    #     if not is_exists_user:
    #         raise forms.ValidationError('کاربری با مشخصات وارد شده ثبت نام نکرده است')
    #     return user_name


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل'
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خود را وارد نمایید'}),
        label='نام'
    )
    family = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی خود را وارد نمایید'}),
        label='نام خانوادگی'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید'}),
        label='کلمه ورود',
        # validators=[
        #     validators.MinLengthValidator(6,'تعداد کارکترهای کلمه عبور نمی تواند کمتر از 6 باشد')
        # ]
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را مجددا وارد نمایید'}),
        label='تایید کلمه عبور'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user_by_username = User.objects.filter(username=user_name).exists()

        if is_exists_user_by_username:
            raise forms.ValidationError('* این کاربر قبلا ثبت نام کرده است')
        return user_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_email = User.objects.filter(email=email).exists()
        if is_exists_user_by_email:
            raise forms.ValidationError('* ایمیل وارد شده تکراری میباشد')
        return email

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('* کلمه های عبور مغایرت دارند')
        return password
