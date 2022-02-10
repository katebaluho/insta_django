from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from account_app.forms.authorization_form import AuthForm
from account_app.forms.edit_form import EditFormUser, EditProfileForm
from account_app.forms.registration_form import RegistrationForm


def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect("/")
    else:
        form = RegistrationForm()
    context = {
        'registration_form': form
    }
    return render(request, "registration_form.html", context)


def auth_page(request):
    error = False
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                next_page = request.GET.get("next", "/")
                return redirect(next_page)
            error = True
    else:
        form = AuthForm()
    context = {"authorization_form": form, "error": error}
    return render(request, "authorization_form.html", context)


@login_required
def profile_edit_page(request):
    if request.method == 'POST':
        user_form = EditFormUser(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to='/')
    else:
        user_form = EditFormUser(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)

    return render(request, 'profile_edit_form.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def profile_page(request):
    context = {'title': 'Profile User', 'user': request.user, 'profile': request.user.profile}
    return render(request, 'profile.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect(to='home')