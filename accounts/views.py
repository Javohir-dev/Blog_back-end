from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")


class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        context = {
            "form": form,
        }
        return render(request, "signup.html", context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password,
            )
            user.save()
            url = reverse("account:login")
            return redirect(url)
        else:
            url = reverse("account:signup")
            return redirect(url)
