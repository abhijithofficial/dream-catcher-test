from django.forms import ModelForm
from .models import UserData

class UserForm(ModelForm):
    class Meta:
        model = UserData
        fields = ['firstname', 'lastname', 'email', 'phonenumber', 'address']
