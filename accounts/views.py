from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserModel
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model,authenticate, login
from .forms import AccountSignUpForm
from django.contrib.messages.views import SuccessMessageMixin

User = get_user_model()

class SignUpView(SuccessMessageMixin, CreateView): ##SuccessMessageMixin

    form_class = AccountSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
    def get_success_message(self, cleaned_data):
        return "Account created!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = f"Sign Up"
        return context


def guest_login(request):
    guest = User.objects.get(pk=7)
    user = authenticate(request, username="guest", password="iamaguest")
    login(request, user)
    return HttpResponseRedirect("to_do/index/")
