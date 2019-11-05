from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests
from .models import Conexiones
import datetime


def index(request):
    #esto es como el controlador/servicios
    ethereum=get_latest_crypto_price('ETH')
    litecoin=get_latest_crypto_price('LTC')

    context = {'ethereum': ethereum,'ethereumcoins':0.2470,'lite': litecoin,'litecoins':0.5584,'total':ethereum*0.2470+litecoin*0.5584}

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)

    datosip=getGeoDatos(ip)
    if datosip['type']!=None:
        #fechas
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        conexion=Conexiones.objects.filter(fecha__range=(today_min, today_max),ip=datosip['ip'])
        if(len(conexion)>0):
            numerodeconexiones=conexion[0].numeroConexiones+1
            actualizar=Conexiones(pk=conexion[0].pk,numeroConexiones=numerodeconexiones,fecha=datetime.datetime.now(),ip=datosip['ip'],pais=datosip['country_name'],ciudad=datosip['city'],postcode=datosip['zip'],coordenadas=datosip['latitude']+","+datosip['longitude'])
            actualizar.save()
        else:
            c = Conexiones(numeroConexiones='1', fecha=datetime.datetime.now(),ip=datosip['ip'],pais=datosip['country_name'],ciudad=datosip['city'],postcode=datosip['zip'],coordenadas=datosip['latitude']+datosip['longitude'])
            c.save()
    
    return render(request, 'index.html',context)



def llamada(request):
    #esto es como el controlador/servicios
    return HttpResponse("return this string")


def get_latest_crypto_price(crypto):
    url = 'https://api.coinbase.com/v2/prices/'+crypto+'-EUR/sell'
    response = requests.get(url)
    response_json = response.json()
    return float(response_json['data']['amount'])

def getGeoDatos(ip):
    url ="http://api.ipstack.com/"+ip+"?access_key=5214629bd7a2ce39efe99b8bc64741a2"
    response = requests.get(url)
    response_json = response.json()
    return response_json
