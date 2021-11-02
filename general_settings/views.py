from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import General_settings, BracketSSContribEE
from .forms import GeneralInfoForm, BracketSSContribEEForm
from django.contrib import messages


def general_info(request):
    data = get_object_or_404(General_settings, pk=1)
    form = GeneralInfoForm(request.POST or None, instance=data)

    if form.is_valid():
        form.save()
        messages.success(request, "Company info was successfully updated.")
        request.session['main_company'] = data.main_company
        return redirect('general-info')

    context = {
        'title': 'VS Payroll Management',
        "page_nick": 'general-info',
        "head": "General Settings",
        "form": form,
        "main_company": data
    }
    return render(request, "gs_home.html", context)


def pf_rates(request):
    ee_pf_contrib = BracketSSContribEE.objects.all()

    context = {
        'title': 'VS Payroll Management',
        "page_nick": "pf-rates",
        "head": "Employee PF Contribution",
        "ee_pf_contrib": ee_pf_contrib
    }
    return render(request, "gs_eecontribss.html", context)


def pf_rates_create(request):
    form = BracketSSContribEEForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = BracketSSContribEEForm()
        return redirect('pf-rates')

    context = {
        'title': 'VS Payroll Management System',
        'page_nick': 'pf-rates',
        'form': form
    }
    return render(request, 'gs_home.html', context)


def pf_rates_delete(request, id):
    obj = get_object_or_404(BracketSSContribEE, id=id)
    obj.delete()
    return redirect('pf-rates')


def pf_rates_update(request, id):
    obj = get_object_or_404(BracketSSContribEE, id=id)
    form = BracketSSContribEEForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('pf-rates')

    context = {
        'title': 'VS Payroll Management System',
        'page_nick': 'pf-rates',
        'form': form
    }
    return render(request, 'gs_home.html', context)


def bank_options(request):
    return HttpResponse('bank options')
