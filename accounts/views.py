from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm


def login_view(request):
    redirect_to = request.POST.get("next", request.GET.get("next", "/"))
    if not request.user.is_authenticated:
        if request.method == "POST":
            # form = AuthenticationForm(request=request, data=request.POST)
            form = LoginForm(request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data.get("username_or_email")
                password = form.cleaned_data.get("password")
                user = authenticate(
                    request, username=username_or_email, password=password
                )
                if user is not None:
                    login(request, user)
                    messages.add_message(
                        request, messages.SUCCESS, f"Welcome, {request.user.username}"
                    )
                    return redirect(redirect_to)
                else:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        "Username or password is incorrect, please try again!",
                    )

        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)

    else:
        return redirect(redirect_to)


@login_required
def logout_view(request):
    logout(request)
    return redirect("/")
