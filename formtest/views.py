from django.shortcuts import render, redirect
# from .forms import RegisterForm
# def index(request):
#     form = RegisterForm()
#     context = { "regForm": form }
#     return render(request, "this_app/index.html", context)

# add this:
from forms import RegistrationForm
# then create an index method:
def index(request):
    form = RegistrationForm() # We will build this class out in just a minute
    context = {
        'myregistrationform': form # Form is the variable name referencing the instance of our RegistrationForm class
    }
    return render(request, 'formtest/index.html', context)

