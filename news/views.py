from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model

from news.models import Token
from news.tasks import send_mail
from .forms import ForgetForm, PasswordChangeForm

User = get_user_model()


class AuthLoginView(LoginView):
    template_name = "login.html"
    success_url = "/"


class ForgetPasswordView(generic.FormView):
    form_class = ForgetForm
    template_name = "password-change.html"

    def form_valid(self, form):
        user = User.objects.filter(username=form.cleaned_data.get("email")).last()
        if user:
            token = Token.objects.create(
                user=user
            )
            send_mail(user.email, token.get_verify_url())
            return redirect("/success/")
        else:
            return redirect("/success/")


class SuccessView(generic.TemplateView):
    template_name = "success.html"


class HomeView(generic.View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponse(f"User : {request.user.username} <a href='/logout/'>Logout</a>")
        else:
            return HttpResponse("Home view")


class VerifyView(generic.View):

    def get(self, request, user_id, token):
        verify = Token.objects.filter(
            user_id=user_id,
            token=token
        ).last()
        if verify:
            context = {}
            context["form"] = PasswordChangeForm()
            return render(request, "password-change.html", context)
        else:
            return redirect("/")

    def post(self, request, user_id, token):
        verify = Token.objects.filter(
            user_id=user_id,
            token=token
        ).last()
        if verify:
            if not verify.expire:
                verify.expire = True
                verify.save()
                form = PasswordChangeForm(request.POST)
                if form.is_valid():
                    password = form.cleaned_data.get("new_password")
                    verify.user.set_password(password)
                    return redirect("/login/")
                else:
                    return redirect("/")
        else:
            return redirect("/")
