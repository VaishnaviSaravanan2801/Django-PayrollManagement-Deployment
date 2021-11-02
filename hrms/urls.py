from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('company-show', views.company_show, name='company-show'),
    path('search-company', views.search_company, name='search-company'),
    path('company-update/<int:pk>', views.company_update, name='company-update'),
    path('print-employees/<int:pk>', views.print_employees, name='print-employees'),
    path('company-rates/<int:pk>', views.company_rates, name='company-rates'),
    path('company-gov-deducts/<int:pk>',
         views.company_gov_deducts, name='company-gov-deducts'),
    path('company-other-options/<int:pk>',
         views.company_other_options, name='company-other-options'),
    path('company-add', views.company_add, name='company-add'),
    path('company-delete/<int:pk>', views.company_delete, name='company-delete')
]
