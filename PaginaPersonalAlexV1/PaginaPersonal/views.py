from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests



def index(request):

    #esto es como el controlador/servicios
    ethereum=get_latest_crypto_price('ETH')
    litecoin=get_latest_crypto_price('LTC')

    context = {'ethereum': ethereum,'ethereumcoins':0.2470,'lite': litecoin,'litecoins':0.5584,'total':ethereum*0.2470+litecoin*0.5584}
    return render(request, 'index.html',context)



def llamada(request):
    #esto es como el controlador/servicios
    return HttpResponse("return this string")


def get_latest_crypto_price(crypto):
    url = 'https://api.coinbase.com/v2/prices/'+crypto+'-EUR/sell'
    response = requests.get(url)
    response_json = response.json()
    return float(response_json['data']['amount'])