from django.shortcuts import render, redirect
from .models import PinDrop,Countries
from django.contrib.gis.geos import Point
from .forms import newPinForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core.serializers import serialize
from django.http import HttpResponse
from django.db import connection
import json

def geogramhome(request):
    if request.method == 'POST':
        form = newPinForm(request.POST, request.FILES)
        if form.is_valid():

            lat = float(form.cleaned_data['latitude'])
            lon = float(form.cleaned_data['longitude'])
            pinloc = Point([lon,lat])

            PinDrop.objects.create(pinuser=request.user,pinphoto=form.cleaned_data['pinimage'],pinbody=form.cleaned_data['pinbody'],pinlocation=pinloc)
            return redirect('geogram:gghome')
        else:
            form = newPinForm()
            pindrops = PinDrop.objects.order_by('-pindate')
            return render(request,'geogram/home.html',{'pins':pindrops,'form':form})
    else:
        form = newPinForm()
        pindrops = PinDrop.objects.order_by('-pindate')
        return render(request,'geogram/home.html',{'pins':pindrops,'form':form})

def logout_request(request):
	logout(request)
	return redirect('geogram:gghome')

def pins_request(request):
    pins = serialize('geojson',PinDrop.objects.all())
    return HttpResponse(pins,content_type='json')

def getpin(request):
    if request.method == 'POST':
        index = request.POST['pk']
        pin = serialize('json',PinDrop.objects.filter(pk=index))
        return HttpResponse(pin,content_type='json')

def getstats(request):
    pins = PinDrop.objects.order_by('pindate')

    country_dict = {}
    pins_dict = {}
    stats = {}
    stats['country_stats'] = {}
    stats['user_stats'] = {}
    stats['total_pins'] = {}
    stats['total_pins']['labels'] = []
    stats['total_pins']['data'] = []
    stats['user_stats']['labels'] = []
    stats['user_stats']['data'] = []
    stats['country_stats']['labels'] = []
    stats['country_stats']['data'] = []
    for pin in pins:
        intersectcheck = Countries.objects.filter(geom__intersects=Point([pin.pinlocation.x,pin.pinlocation.y]))
        for country in intersectcheck:
            c_name = country.name
            if c_name in country_dict:
                country_dict[c_name] += 1
            else:
                country_dict[c_name] = 1

        pinsdate = pin.shortpindate()
        if pinsdate in pins_dict:
            pins_dict[pinsdate] += 1
        else:
            pins_dict[pinsdate] = 1

    for key in country_dict:
        stats['country_stats']['labels'].append(key)
        stats['country_stats']['data'].append(country_dict[key])

    totalpins = 0
    for key in pins_dict:
        totalpins += pins_dict[key]
        stats['total_pins']['labels'].append(key)
        stats['total_pins']['data'].append(totalpins)

    if request.user.is_authenticated:
        userpins = PinDrop.objects.filter(pinuser_id=request.user.pinuser_id)
        country_dict.clear()
        for pin in userpins:
            intersectcheck = Countries.objects.filter(geom__intersects=Point([pin.pinlocation.x,pin.pinlocation.y]))
            for country in intersectcheck:
                c_name = country.name
                if c_name in country_dict:
                    country_dict[c_name] += 1
                else:
                    country_dict[c_name] = 1

        for key in country_dict:
            stats['user_stats']['labels'].append(key)
            stats['user_stats']['data'].append(country_dict[key])
    else:
        stats['user_stats']['labels'].append(0)
        stats['user_stats']['data'].append(0)

    return HttpResponse(json.dumps(stats))

def stats(request):
    return render(request,'geogram/stats.html')
