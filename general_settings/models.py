from django.db import models

# Create your models here.


class General_settings(models.Model):
    main_company = models.CharField(default="company", max_length=255)
    template_name = models.CharField(default="Company Inc.", max_length=255)
    company_address = models.CharField(default="Company Location", max_length=255)
    company_contacts = models.CharField(default="02 xxx-xxxx / 02 xxx-xxxx", max_length=255)

    def __str__(self):
        return f'{self.main_company}'


class BracketSSContribEE(models.Model):
    contrib_amount = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    ranged = models.CharField(max_length=100)
