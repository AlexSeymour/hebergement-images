from django.shortcuts import render, redirect, HttpResponse
from user.forms import RegistrationForm
from django.contrib import messages


def registration(request):
    if request.method == 'POST':

        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)

            user.save()
            messages.add_message(request, messages.SUCCESS, "Vous êtes désormais inscris")
            return redirect('/')

    else:
        user_form = RegistrationForm()
    return render(request, "user/registration.html", {'form': user_form})

