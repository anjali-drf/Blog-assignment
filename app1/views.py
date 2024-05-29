from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.views import LoginView
from django.views import View


def home(request):
    return render(request,'home.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        auth_login(self.request, form.get_user())
        return redirect('home')  # Redirect to home page after successful login


class CustomLogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect('home')