from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wallet
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.
def home(request):
    return render(request, 'home.html')

def manage(request):
    wallets = Wallet.objects.all()
    return render(request, 'manage.html', {'wallets': wallets,})

def add_wallet(request):
    name = request.POST.get('name')
    bank = request.POST.get('bank')
    wallet_type = request.POST.get('wallet_type')
    value = request.POST.get('value')

    if len(name.strip()) == 0 or len(value.strip()) == 0:
        messages.add_message(request, constants.WARNING, 'Make sure all fields are filled in')
        return redirect('/finance_profile/manage/')


    wallet = Wallet(
        name=name,
        bank=bank,
        wallet_type=wallet_type,
        value=value,
    )

    wallet.save()

    messages.add_message(request, constants.SUCCESS, 'Wallet successfully added')
    return redirect('/finance_profile/manage/')