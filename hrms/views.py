from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Company, Company_rates
from employee.models import Employee, Employee_hiring_details
from logs.models import Logs
from general_settings.models import General_settings

from .forms import CompanyAddForm, CompanyRates, CompanyGovDeduct, CompanyOtherOptions

from django.contrib import messages
import xlwt
from datetime import datetime, timedelta
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def dashboard(request):
    gen_settings = General_settings.objects.get(id=1)
    context = {
        'main_company': gen_settings.main_company,
        'title': 'VS Payroll Management System',
        'head': 'Dashboard'
    }
    
    if gen_settings:
        request.session['main_company'] = gen_settings.main_company
    else:
        request.session['main_company'] = ""
    return render(request, 'dashboard.html', context)

# print employees excel
@login_required
def search_company(request):

    searched_company = request.POST.get("company")
    print(searched_company)
    result = Company.objects.filter(
        Q(company_name__icontains=searched_company)
    )
    # result = Company.objects.all()
    print(result)
    result_count = result.count()
    search_head = "Search result: 0"
    if result_count > 0:
        search_head = "Search result: " + str(result_count)
    print(result_count)
    gen_settings = General_settings.objects.get(id=1)
    context = {
        'main_company': gen_settings.main_company,
        'title': 'VS Payroll Management System',
        'head': search_head,
        'search_results': result
    }

    return render(request, 'search_results.html', context)

@login_required
def print_employees(request, pk):
    response = HttpResponse(content_type='text/ms-excel')
    company = get_object_or_404(Company, pk=pk)
    
    file_name = f"{company.company_name}'s employees.xls"
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('employee_list')

    style = 'align: wrap on, vert centre, horiz center; font: bold on'
#    ws.row(0).write(0, value, xlwt.Style.easyxf(style))
    ws.write_merge(0, 1, 0, 15, f"VS Manpower- {company.company_name}'s Employee List",
                   xlwt.Style.easyxf(style))

    row_num = 3

    # style = 'align: wrap on, vert centre, horiz center; font: bold on'
    font_style = xlwt.Style.easyxf(style)
    columns = ['Firstname',  'Middlename', 'Lastname',  'Date Hired', 'Date End', 'Birthday', 'PF',
               'ESI', 'CONTACT NUMBER']
               
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    style = 'align: wrap on, vert centre, horiz center'
    font_style = xlwt.Style.easyxf(style,num_format_str='YY-MM-DD')

    rows = Employee.objects.filter(company=pk).values_list(
        'first_name', 'middle_name', 'last_name',  'date_hired', 'contract_expiration', 'date_of_birth', 'sss_no',
        'pagibig_no', 'phone'
    )
    
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    action = f"{company} employees was successfully generated."
    Logs.objects.create(action=action, action_by=request.user,
                        action_date=datetime.now())



    wb.save(response)
    return response

# read company

@login_required
def company_show(request):
    companies = Company.objects.all()
    gen_settings = General_settings.objects.filter(id=1).first()
    if gen_settings:
        request.session['main_company'] = gen_settings.main_company
    else:
        request.session['main_company'] = ""

    context = {
        'title': 'VS Payroll Management System',
        'head': 'Companies',
        'companies': companies
    }
    return render(request, 'all_companies.html', context)

# update company

@login_required
def company_update(request, pk):
    company = get_object_or_404(Company, id=pk)
    if request.method == 'POST':
        form = CompanyAddForm(request.POST or None, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, f'Company was successfully updated.')
            return redirect('company-update', pk=pk)
    else:
        form = CompanyAddForm(instance=company)


    gen_settings = General_settings.objects.get(id=1)
    context = {
        'main_company': gen_settings.main_company,
        'title': 'VS Payroll Management System',
        'head': 'Update Company',
        'form': form,
        'company_id': pk
    }
    return render(request, 'company_update.html', context)

@login_required
def company_rates(request, pk):
    company = get_object_or_404(Company_rates, company=pk)
    # return HttpResponse(pk)
    if request.method == 'POST':
        form = CompanyRates(request.POST or None, instance=company)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Company rates was successfully updated.')
            return redirect('company-rates', pk=pk)
    else:
        form = CompanyRates(instance=company)

    gen_settings = General_settings.objects.get(id=1)
    context = {
        'main_company': gen_settings.main_company,
        'title': 'VS Payroll Management System',
        'head': 'Update Rates',
        'form': form,
        'company_id': pk
    }
    return render(request, 'company_update.html', context)

@login_required
def company_gov_deducts(request, pk):
    company = get_object_or_404(Company_rates, company=pk)
    
    if request.method == 'POST':
        form = CompanyGovDeduct(request.POST or None, instance=company)
        if form.is_valid():
            form.save()

            action = f"{company} deductions has been updated. sss={request.POST['sss']}, philhealth={request.POST['philhealth']}, pagibig={request.POST['pagibig']}"
            Logs.objects.create(action=action, action_by=request.user, action_date=datetime.now())

            messages.success(request, f'Company Government deductions was successfully updated.')
            return redirect('company-gov-deducts', pk=pk)
    else:
        form = CompanyGovDeduct(instance=company)

    gen_settings = General_settings.objects.get(id=1)
    context = {
        'main_company': gen_settings.main_company,
        'title': 'VS Payroll Management System',
        'page_nick': 'gov-deducts',
        'head': 'Update Government Deductions',
        'form': form,
        'company_id': pk
    }
    return render(request, 'company_update.html', context)

@login_required
def company_other_options(request, pk):
    company = get_object_or_404(Company_rates, company=pk)
    # return HttpResponse(pk)
    if request.method == 'POST':
        form = CompanyOtherOptions(request.POST or None, instance=company)
        if form.is_valid():
            form.save()
            Logs.objects.create(
                action=f"{company.company} Other options was successfully updated", action_by=request.user, action_date=datetime.now())

            messages.success(
                request, f'Company other options was successfully updated.')
            return redirect('company-other-options', pk=pk)
    else:
        form = CompanyOtherOptions(instance=company)

    gen_settings = General_settings.objects.get(id=1)
    context = {
        'main_company': gen_settings.main_company,
        'title': 'VS Payroll Management System',
        'page_nick': 'other-opt',
        'head': 'Update Government Deductions',
        'form': form,
        'company_id': pk
    }
    return render(request, 'company_update.html', context)


@login_required# create company
def company_add(request):
    # user = get_object_or_404(User, user=request.user)
    if request.method == 'POST':
        form = CompanyAddForm(request.POST)
        if form.is_valid():
            company = form.save()
            action = f"created company '{company.company_name}'"
            Logs.objects.create(action=action, action_by=request.user, action_date=datetime.now())

            messages.success(
                request, f'New company %s was successfully created.' % (company.company_name))
            return redirect('company-show')
    else:
        form = CompanyAddForm()
        
    gen_settings = General_settings.objects.get(id=1)
    context = {
        'main_company': gen_settings.main_company,
        'title': 'VS Payroll Management System',
        'head': 'Add Company',
        'form': form
    }
    return render(request, 'company_add.html', context)


@login_required
def company_delete(request, pk):
    # if request.method == 'POST':
    company = Company.objects.filter(pk=pk).first()
    action = f"deleted company '{company.company_name}'"
    company.delete()
    Logs.objects.create(action=action, action_by=request.user, action_date=datetime.now())

    messages.success(request, f'Company was successfully deleted.')
    return redirect('company-show')
    # return redirect('company-show')
