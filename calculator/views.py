from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import request
from django.core.paginator import Paginator

from calculator.models import *

# Create views
def GenSetting(request):

    gs = GeneralSettings.objects.all()
    paginator = Paginator(gs, 6)
    page_number = request.GET.get('page')
    gs = paginator.get_page(page_number)
    context = {'gs': gs}
    return render(request, 'general_settings.html', context)

def AddGenSetting(request):
    if request.method == 'POST':
        electricity_cost = request.POST.get('electricity_cost')
        rent_cost = request.POST.get('rent_cost')

        gs = GeneralSettings(
            electricity_cost=electricity_cost,
            rent_cost=rent_cost
        )
        gs.save()
        return redirect('generalsettings')

    return render(request, 'general_settings.html')


def EditGenSetting(request):
    gs = GeneralSettings.objects.all()
    context = {'gs': gs}
    return redirect(request, 'general_settings.html', context)


def UpdGenSetting (request, id):
    if request.method == 'POST':
        gs = GeneralSettings.objects.get(pk=id)

        gs.electricity_cost = request.POST.get('electricity_cost')
        gs.rent_cost = request.POST.get('rent_cost')

        gs.save()
        return redirect('generalsettings')
    return render(request, 'general_settings.html')


def DelGenSetting(request, id):
    gs = GeneralSettings.objects.get(pk=id)
    gs.delete()
    context = {'gs': gs}
    return redirect('generalsettings')

