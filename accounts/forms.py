from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserModel
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountSignUpForm(UserCreationForm): 

    class Meta: 
        model = Account
        fields = ['username', 'email']


