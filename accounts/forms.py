from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    base_class = 'w-full px-4 py-3 rounded-lg bg-white/30 border border-blue-900 text-white placeholder-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500'
    name = forms.CharField(max_length=150, label='Name',
                           widget=forms.TextInput(attrs={'class': base_class}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': base_class}))
    phone = forms.CharField(max_length=20, label='Telefone',
                           widget=forms.TextInput(attrs={'class': base_class}))

    class Meta:
        model = User
        fields = ('name', 'email', 'phone', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': self.base_class})
        self.fields['password2'].widget.attrs.update({'class': self.base_class})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['name']
        if commit:
            user.save()
            Profile.objects.create(user=user, phone=self.cleaned_data['phone'])
        return user


class LoginForm(AuthenticationForm):
    """Authentication form com classes do Tailwind"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': SignUpForm.base_class})
