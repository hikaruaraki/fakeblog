from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from .models import CustomUser
from django.http import HttpResponse,HttpResponseRedirect

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:success')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)


class SignUpSuccessView(TemplateView):
    template_name = 'success.html'

def password(request):
    return render(request,'password.html')

def log_success(request):
    return render(request,'log_success.html')