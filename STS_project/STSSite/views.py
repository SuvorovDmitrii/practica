from django.shortcuts import render, redirect
from django import forms
from django.views.generic import DetailView

from .models import *
from .forms import UserRegistrationForm, CreateOrder

def index(request):
    usluga = Uslugi.objects.all
    return render(request, 'index.html', context={'usluga':usluga})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/login.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})

def order_add(request):
    form = CreateOrder

    if request.method == "POST":
        form = CreateOrder(request.POST)
        if form.is_valid():
            order_form = form.save(commit=False)
            order_form.person = request.user
            order_form.save()
            return redirect(order_add)

    return render(request, 'order_create.html', {
        'form': form
    })

class ShowUserPageView(DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_object(self):
        # users = User.objects.filter(id__exact = self.request.user.id)
        # patronomyc = users.get(Person.patronomyc)
        try:
            person = User.objects.get(user=self.request.user.id)
        except:
            person = None
        return person
# Create your views here.
