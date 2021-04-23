from django.shortcuts import render, redirect 
from forms import RegistrationForm
from .models import User
# then create an index method:
def index(request):
    form = RegistrationForm
    context = {
        'myregistrationform': form # Form is the variable name referencing the instance of our RegistrationForm class
    }
    return render(request, 'formtest/index.html', context)

