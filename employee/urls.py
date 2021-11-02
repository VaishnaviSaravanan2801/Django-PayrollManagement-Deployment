from django.urls import path
from .import views

urlpatterns = [
    path('employee-show', views.employee_show, name='employee-show'),
    path('search-employees', views.search_employees, name='search-employees'),
    path('employee-add', views.employee_add, name='employee-add'),
    path('employee-update/<int:pk>', views.employee_update, name='employee-update'),

    path('employee-preferences/<int:pk>',
         views.employee_preferences, name='employee-preferences'),

    path('employee-records/<int:pk>',
         views.employee_records, name='employee-records'),

    path('emp-record-delete/<int:pk>/<int:emp_id>',
         views.emp_record_delete, name='emp-record-delete'),

    path('employee-hiring-details/<int:pk>',
         views.employee_hiring_details, name='employee-hiring-details'),

    path('employee-biodata/<int:pk>',
         views.employee_biodata, name='employee-biodata'),

    path('employee-resume/<int:pk>', views.employee_resume, name='employee-resume'),

    path('employee-company-loan/<int:pk>',
         views.employee_company_loan, name='employee-company-loan'),

    path('employee-pagibig-loan/<int:pk>',
         views.employee_pagibig_loan, name='employee-pagibig-loan'),

    path('employee-comloan-contrib/<int:pk>/<int:comloan>',
         views.employee_comloan_contrib, name='employee-comloan-contrib'),


    path('employee-valeloan-contrib/<int:pk>/<int:comloan>',
              views.employee_valeloan_contrib, name='employee-valeloan-contrib'),

    path('employee-vale/<int:pk>', views.employee_vale, name='employee-vale'),

    path('employee-pagibigloan-contrib/<int:pk>/<int:comloan>',
         views.employee_pagibigloan_contrib, name='employee-pagibigloan-contrib'),

    path('employee-uniform/<int:pk>',
         views.employee_uniform, name='employee-uniform'),

    path('employee-medical-contrib/<int:pk>/<int:comloan>',
              views.employee_medical_contrib, name='employee-medical-contrib'),

    path('employee-medical/<int:pk>',
         views.employee_medical, name='employee-medical'),

    path('employee-canteen-contrib/<int:pk>/<int:comloan>',
              views.employee_canteen_contrib, name='employee-canteen-contrib'),

    path('employee-canteen/<int:pk>',
         views.employee_canteen, name='employee-canteen'),

    path('employee-gatepass-contrib/<int:pk>/<int:comloan>',
              views.employee_gatepass_contrib, name='employee-gatepass-contrib'),

    path('employee-gatepass/<int:pk>',
         views.employee_gatepass, name='employee-gatepass'),

    path('employee-acceptance/<int:pk>',
         views.employee_acceptance, name='employee-acceptance'),

    path('employee-leave-absence/<int:pk>',
         views.employee_leave_absence, name='employee-leave-absence'),

    path('update-record/<int:record>',
         views.update_record, name='update-record'),

    path('employee-endorsement-letter/<int:pk>',
         views.employee_endorsement_letter, name='employee-endorsement-letter'),

    path('employee-upload-picture/<int:pk>',
         views.employee_upload_picture, name='employee-upload-picture'),

    path('employee-requirements/<int:pk>',
         views.employee_requirements, name='employee-requirements'),

    path('employee-memo/<int:pk>',
         views.employee_memo, name='employee-memo'),

    path('memo-delete/<int:pk>',
         views.memo_delete, name='memo-delete'),

]
