from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    contact_person = models.CharField(max_length=100)
    fax = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.company_name}'

    def get_company_rates(self):
        return Company_rates.objects.filter(company=self).first()


def create_company_rates(sender, **kwargs):
    if kwargs['created']:
        employee_resume = Company_rates.objects.create(company=kwargs['instance'])


post_save.connect(create_company_rates, sender=Company)


class Company_rates(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_rates')
    base_rate = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    base_training_rate = models.DecimalField(
        max_digits=7, decimal_places=2, null=True)
    activate_rates = models.BooleanField(default=False)
    activate_training_rate = models.BooleanField(default=False)

    ecola_rate = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0.0)
    activate_ecola = models.BooleanField(default=True)
    activate_overtime = models.BooleanField(default=True)
    activate_1_25_overtime = models.BooleanField(default=True)
    activate_rest_day = models.BooleanField(default=True)
    activate_holiday = models.BooleanField(default=True)
    activate_special = models.BooleanField(default=True)
    activate_night_differential = models.BooleanField(default=True)
    activate_thirteenth_month = models.BooleanField(default=True)
    activate_tardiness = models.BooleanField(default=True)
    activate_sil = models.BooleanField(default=True)
    activate_tshirt = models.BooleanField(default=True)
    activate_rf = models.BooleanField(default=True)
    activate_house = models.BooleanField(default=True)
    activate_misc = models.BooleanField(default=True)
    activate_gatepass = models.BooleanField(default=True)
    activate_medical = models.BooleanField(default=True)
    activate_pants = models.BooleanField(default=True)
    activate_vale = models.BooleanField(default=True)
    activate_uniform = models.BooleanField(default=True)
    activate_company_loan = models.BooleanField(default=True)
    activate_pagibig_loan = models.BooleanField(default=True)
    activate_sss_loan = models.BooleanField(default=True)
    activate_canteen = models.BooleanField(default=True)
    activate_service_fee = models.BooleanField(default=True)
    activate_sunday = models.BooleanField(default=True)
    activate_allowance = models.BooleanField(default=True)
    activate_adjustment = models.BooleanField(default=True)
    activate_transpo_allowance = models.BooleanField(default=True)
    
    sss = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    philhealth = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    pagibig = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.company} rates'
