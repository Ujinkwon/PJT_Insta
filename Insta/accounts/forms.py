from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ID'
        }
       ) 
    )
    password1 = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호(8자 이상)'
            }
        )
    )
    password2 = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 확인'
            }
        )
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '전화번호, 사용자 이름 또는 이메일',
        }
       ) 
    )
    password = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호'
            }
        )
    )
    class Meta:
        model = get_user_model()
        fields = ('username', 'password',)
