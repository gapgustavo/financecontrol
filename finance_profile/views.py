from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wallet, Categorie
from django.contrib import messages
from django.contrib.messages import constants
from useful.useful import sum_total


# Create your views here.
def home(request):
    return render(request, 'home.html')

def manage(request):
    wallets = Wallet.objects.all()
    categories = Categorie.objects.all()
    total_wallets = sum_total(wallets, 'value')
    return render(request, 'manage.html', {'wallets': wallets, 'total_wallets': total_wallets, 'categories': categories})

def add_wallet(request):
    name = request.POST.get('name')
    bank = request.POST.get('bank')
    wallet_type = request.POST.get('wallet_type')
    value = request.POST.get('value')

    if len(name.strip()) == 0 or len(value.strip()) == 0:
        messages.add_message(request, constants.WARNING, 'Make sure all WALLET fields are filled in')
        return redirect('/finance_profile/manage/')


    wallet = Wallet(
        name=name,
        bank=bank,
        wallet_type=wallet_type,
        value=value,
    )

    wallet.save()

    messages.add_message(request, constants.SUCCESS, 'WALLET successfully added')
    return redirect('/finance_profile/manage/')

def delete_wallet(request, id):
    wallet_id = Wallet.objects.get(id=id)
    wallet_id.delete()
    messages.add_message(request, constants.ERROR, 'Wallet DELETED')
    return redirect('/finance_profile/manage/')


def add_categorie(request):
    categorie = request.POST.get('categorie')
    essential = bool(request.POST.get('essential'))

    categorie = Categorie(
        categorie=categorie,
        essential=essential,
    )

    if len(str(categorie)) == 0:
        messages.add_message(request, constants.WARNING, 'Make sure all CATEGORIES fields are filled in')
        return redirect('/finance_profile/manage/')

    categorie.save()

    messages.add_message(request, constants.SUCCESS, 'CATEGORIE successfully added')
    return redirect('/finance_profile/manage/')