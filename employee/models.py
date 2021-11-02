from django.db import models
from hrms.models import Company
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator


class Employee(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='company')
    emp_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    provincial_address = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    date_hired = models.DateField(null=True)
    contract_expiration = models.DateField(null=True)

    # sss_bracket = models.CharField(max_length=50)
    gov_deductions_to_implement = models.CharField(max_length=255, default="")
    sss_option = models.CharField(max_length=255, default="")
    sss_bracket = models.DecimalField(max_digits=7, decimal_places=2, default="0")
    sss_value = models.DecimalField(max_digits=7, decimal_places=2, default="0")
    pagibig_value = models.DecimalField(max_digits=7, decimal_places=2, default="0")
    philhealth_value = models.DecimalField(max_digits=7, decimal_places=2, default="0")

    sss_no = models.CharField(max_length=10, validators=[MinLengthValidator(10)], default="")
    pagibig_no = models.CharField(max_length=10, validators=[MinLengthValidator(10)], default="")
    philhealth_no = models.CharField(max_length=12,validators=[MinLengthValidator(12)], default="")
    tin_no = models.CharField(max_length=12, validators=[MinLengthValidator(12)], default="")
    civil_status = models.CharField(max_length=255)
    citizenship = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255, default="")

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def get_hiring_details(self):
        return Employee_hiring_details.objects.filter(employee=self).first()


# employee_preferences

def create_employee_preferences(sender, **kwargs):
    if kwargs['created']:
        employee_preferences = Employee_preferences.objects.create(
            employee=kwargs['instance'])

# Employee_hiring_details


def create_hiring_details(sender, **kwargs):
    if kwargs['created']:
        employee_hiring_details = Employee_hiring_details.objects.create(
            employee=kwargs['instance'])

# Employee_resume


def create_resume(sender, **kwargs):
    if kwargs['created']:
        employee_resume = Employee_resume.objects.create(
            employee=kwargs['instance'])


def create_picture(sender, **kwargs):
    if kwargs['created']:
        employee_picture = Employee_picture.objects.create(
            employee=kwargs['instance'])

def create_requirements(sender, **kwargs):
    if kwargs['created']:
        employee_requirements = Employee_requirements.objects.create(employee=kwargs['instance'])

def create_acceptance(sender, **kwargs):
    if kwargs['created']:
        employee_acceptance = Employee_acceptance.objects.create(employee=kwargs['instance'])


post_save.connect(create_requirements, sender=Employee)


post_save.connect(create_employee_preferences, sender=Employee)
post_save.connect(create_hiring_details, sender=Employee)
post_save.connect(create_resume, sender=Employee)
post_save.connect(create_picture, sender=Employee)
post_save.connect(create_acceptance, sender=Employee)


class Employee_preferences(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_pref')
    spouse = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    spouse_address = models.CharField(max_length=255, blank=True, null=True)
    character_reference_name = models.CharField(max_length=255)
    character_reference_address = models.CharField(max_length=255)
    character_reference_phone = models.CharField(max_length=255)

    def __str__(self):
        return f'{ self.employee } - Preferences'


class Employment_record(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_rec')
    from_date = models.DateField()
    to_date = models.DateField()
    company = models.CharField(max_length=255, default="")
    position = models.CharField(max_length=255)

    def __str__(self):
        return f'{ self.employee } - Record'


class Employee_hiring_details(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_hr')
    rate = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    training_rate = models.DecimalField(
        max_digits=7, decimal_places=2, null=True)
    bank = models.CharField(max_length=255)
    atm = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    overtime_formula = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    def __str__(self):
        return f'{ self.employee } - Hiring Details'


class Employee_resume(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_resume')
    resume = models.FileField(blank=True, upload_to='resume')

    def __str__(self):
        return f'{self.employee} - resume'


class Employee_picture(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_picture')
    picture = models.ImageField(upload_to='media/')

    def __str__(self):
        return f'{self.employee} - picture'



class Employee_company_loan(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_com_loan')
    load_amount = models.DecimalField(
        max_digits=7, decimal_places=2, null=True)
    rate_to_deduct = models.DecimalField(
        max_digits=7, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{ self.employee } - Company Loan'


class Employee_comloan_contrib(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_comload_contrib')
    payroll = models.IntegerField(default=0)
    company_loan = models.ForeignKey(
        Employee_company_loan, on_delete=models.CASCADE, related_name='employee_company')
    cut_off_date = models.DateField()
    contribution_collected = models.DecimalField(
        max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{ self.employee } {self.id} - company loan contrib'


class Employee_pagibig_loan(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_pag_loan')
    load_amount = models.DecimalField(
        max_digits=7, decimal_places=2, null=True)
    rate_to_deduct = models.DecimalField(
        max_digits=7, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{ self.employee } - Pagibig Loan'


class Employee_pagibigloan_contrib(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_pagibigload_contrib')
    payroll = models.IntegerField(default=0)
    pagibig_loan = models.ForeignKey(
        Employee_pagibig_loan, on_delete=models.CASCADE, related_name='employee_pagibigloan_company')
    cut_off_date = models.DateField()
    contribution_collected = models.DecimalField(
        max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{ self.employee } {self.id} - pagibig loan contrib'


class Employee_vale(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_vale')
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    rate_to_deduct = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{ self.employee } - Vale'


class Employee_valeloan_contrib(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_valeloan_contrib')
    payroll = models.IntegerField(default=0)
    vale_loan = models.ForeignKey(
        Employee_vale, on_delete=models.CASCADE, related_name='employee_valeloan_company')
    cut_off_date = models.DateField()
    contribution_collected = models.DecimalField(
        max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{ self.employee } {self.id} - vale load contrib'


class Employee_sss(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_sss')
    cut_off_date = models.DateField()
    contribution_collected = models.DecimalField(
        max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{ self.employee } - sss'


class Employee_pagibig(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_pagibig')
    cut_off_date = models.DateField()
    contribution_collected = models.DecimalField(
        max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{ self.employee } - pagibig'


class Employee_uniform(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_uniform')
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    rate_to_deduct = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{ self.employee } - Uniform'


class Employee_medical(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_medical')
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    rate_to_deduct = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{ self.employee } - Medical'


class Employee_medical_contrib(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_medical_contrib')
    payroll = models.IntegerField(default=0)
    medical_loan = models.ForeignKey(
        Employee_medical, on_delete=models.CASCADE, related_name='employee_medical_company')
    cut_off_date = models.DateField()
    contribution_collected = models.DecimalField(
        max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{ self.employee } {self.id} - medical loan contrib'


class Employee_canteen(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_canteen')
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    rate_to_deduct = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{ self.employee } - Canteen'


class Employee_canteen_contrib(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_canteen_contrib')
    payroll = models.IntegerField(default=0)
    canteen_loan = models.ForeignKey(
        Employee_canteen, on_delete=models.CASCADE, related_name='employee_canteen_company')
    cut_off_date = models.DateField()
    contribution_collected = models.DecimalField(
        max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{ self.employee } {self.id} - canteen loan contrib'


class Employee_gatepass(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_gatepass')
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    rate_to_deduct = models.DecimalField(max_digits=7, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{ self.employee } - Gatepass'


class Employee_gatepass_contrib(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_gatepass_contrib')
    payroll = models.IntegerField(default=0)
    gatepass_loan = models.ForeignKey(
        Employee_gatepass, on_delete=models.CASCADE, related_name='employee_gatepass_company')
    cut_off_date = models.DateField()
    contribution_collected = models.DecimalField(
        max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{ self.employee } {self.id} - gatepass loan contrib'


class Employee_acceptance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_acceptance')
    employment_status = models.CharField(null=True,max_length = 50)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    position = models.CharField(null=True, max_length = 50)
    salary_per_day = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    salary_per_month = models.DecimalField(null=True, max_digits=7, decimal_places=2)


class Employee_leave_history(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_leave_history')
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_days = models.IntegerField(default=0)


class Employee_citizenship(models.Model):
    citizenship = models.CharField(max_length = 50)


class Employee_requirements(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_requirements')
    nbi = models.BooleanField(default=False)
    barangay = models.BooleanField(default=False)
    medical = models.BooleanField(default=False)
    sss_id = models.BooleanField(default=False)
    ph_id = models.BooleanField(default=False)
    birth_certificate = models.BooleanField(default=False)
    atm_application = models.BooleanField(default=False)
    pagibig_id = models.BooleanField(default=False)
    hs_diploma = models.BooleanField(default=False)
    college_diploma = models.BooleanField(default=False)
    employee_contract = models.BooleanField(default=False)
    certificate_of_employment = models.BooleanField(default=False)
    photo = models.BooleanField(default=False)


class Employee_memo(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='employee_emo')
    memo = models.FileField(blank=True, upload_to='memo')

    def __str__(self):
        return f'{ self.employee } - memo ({self.memo})'
