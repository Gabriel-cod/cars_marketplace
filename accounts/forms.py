from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-control'
            })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'name@example.com'
            })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
            })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
            })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request = ..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control'
        })