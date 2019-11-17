from django.shortcuts import render
from chatterbot import ChatBot

# Create your views here.
from django.http import HttpResponse
import requests
from .models import Conexiones
import datetime
from django.conf import settings


def index(request):
    if request.POST.get('mensaje'):
        chatbot = ChatBot(**settings.CHATTERBOT)
        if( 'conversacion' in request.session):
            conversacionbot=request.session['conversacion']
            conversacionbot.append(request.POST.get('mensaje'))
            conversacionbot.append(str(chatbot.get_response(str(request.POST.get('mensaje')))))
            request.session['conversacion']=conversacionbot

        else:
            conversacionbot=[]
            conversacionbot.append(request.POST.get('mensaje'))
            conversacionbot.append(str(chatbot.get_response(str(request.POST.get('mensaje')))))
            request.session['conversacion']=conversacionbot
    else:
        conversacionbot=["Saludos soy la IA de alex, en que puedo ayudarte"]
        request.session['conversacion']=conversacionbot


    ethereum=get_latest_crypto_price('ETH')
    litecoin=get_latest_crypto_price('LTC')


    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for and x_forwarded_for is not None:
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
            actualizar=Conexiones(pk=conexion[0].pk,numeroConexiones=numerodeconexiones,fecha=datetime.datetime.now(),ip=datosip['ip'],pais=datosip['country_name'],ciudad=datosip['city'],postcode=datosip['zip'],coordenadas=str(datosip['latitude'])+","+str(datosip['longitude']))
            actualizar.save()
        else:
            c = Conexiones(numeroConexiones='1', fecha=datetime.datetime.now(),ip=datosip['ip'],pais=datosip['country_name'],ciudad=datosip['city'],postcode=datosip['zip'],coordenadas=str(datosip['latitude'])+','+str(datosip['longitude']))
            c.save()
    
    conexiones = list(Conexiones.objects.all())
    print(conexiones)
    charConexiones={}
    for conexion in conexiones:
        if str(conexion.fecha.year)+", "+str(conexion.fecha.month)+", "+str(conexion.fecha.day) in charConexiones:
            charConexiones[str(conexion.fecha.year)+", "+str(conexion.fecha.month)+", "+str(conexion.fecha.day)]=charConexiones[str(conexion.fecha.year)+", "+str(conexion.fecha.month)+", "+str(conexion.fecha.day)]+1
        else:
            charConexiones[str(conexion.fecha.year)+", "+str(conexion.fecha.month)+", "+str(conexion.fecha.day)]=1
    print(charConexiones)
    stringparaelchar="["
    index=0
    for key in charConexiones:
        if(index!=0):
            stringparaelchar=stringparaelchar+","
        stringparaelchar=stringparaelchar+"[ new Date("+str(key)+"), "+str(charConexiones[key])+"]"
        index=1
    stringparaelchar=stringparaelchar+"]"
    print(stringparaelchar)

    #conexiones="[[ new Date(2013, 9, 4), 6 ],[ new Date(2013, 9, 5), 3],[ new Date(2013, 9, 12), 1 ],[ new Date(2013, 9, 13), 2 ]]"
    context = {'ethereum': ethereum,'ethereumcoins':0.2470,'lite': litecoin,'litecoins':0.5584,'total':ethereum*0.2470+litecoin*0.5584,"conexiones":stringparaelchar,"chat":conversacionbot}

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
