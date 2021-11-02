from django import forms
from .models import Employee, Employee_preferences, Employment_record, Employee_hiring_details, Employee_resume, Employee_company_loan, Employee_uniform, Employee_medical, Employee_canteen, Employee_gatepass, Employee_vale, Employee_pagibig_loan,  Employee_acceptance, Employee_leave_history, Employee_citizenship, Employee_picture, Employee_requirements, Employee_memo
from hrms.models import Company
from general_settings.models import BracketSSContribEE


class EmployeeAddForm(forms.ModelForm):
	date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
	GENDER = CHOICES = (('', 'Choose gender'),('male', 'Male'), ('female', 'Female'))
	gender = forms.CharField(widget=forms.Select(choices=GENDER))

	def __init__(self, *args, **kwargs):
		super(EmployeeAddForm, self).__init__(*args, **kwargs)
		queryset = Employee_citizenship.objects.values_list('citizenship', flat=True).distinct()
		self.fields['middle_name'].required = False

		CITIZENSHIP = [('', 'Choose citizenship'), ('indian', 'Indian')] + [(citizenship, citizenship) for citizenship in queryset]
		self.fields['citizenship'] = forms.ChoiceField(choices=CITIZENSHIP,  widget=forms.Select(attrs={'onchange': 'Hide()'}))

	CIVIL_STATUS = CHOICES = (('', 'Choose status'),('single', 'Single'), ('married', 'Married'))
	civil_status = forms.CharField(widget=forms.Select(choices=CIVIL_STATUS))
	date_hired = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
	contract_expiration = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))

	SSS_OPTION = CHOICES = (('0', 'Choose Sss Option'),
							('bracket', 'By Range'),
							('manual', 'By manual'),)
	sss_option = forms.CharField(label='PF option', widget=forms.Select(choices=SSS_OPTION, attrs={'onchange': 'HideSSS()'}))

	USE_COM = CHOICES = (
		('', 'Choose Gov Deduction to Implement'),
		('company_base_deductions', 'Company Base Deductions'),
	)
	gov_deductions_to_implement = forms.CharField(
		widget=forms.Select(choices=USE_COM, attrs={'onchange': 'HideGovDeductions()'}))

	brackets_queryset = BracketSSContribEE.objects.all()
	SSS_BRACKET = [('0', 'Choose Bracket')] + [(brackets.contrib_amount, brackets.ranged) for brackets in
											   brackets_queryset]
	sss_bracket = forms.CharField(label='PF Range', widget=forms.Select(choices=SSS_BRACKET))
	philhealth_value = forms.DecimalField(label='Health value')

	sss_no = forms.CharField(label='PF no.', widget=forms.TextInput(attrs={'type': 'number'}), )
	pagibig_no = forms.CharField(label='ESI no.', widget=forms.TextInput(attrs={'type': 'number'}), )
	philhealth_no = forms.CharField(label='Health insurance id', widget=forms.TextInput(attrs={'type': 'number'}), )
	tin_no = forms.CharField(label='Aadhaar No.', widget=forms.TextInput(attrs={'type': 'number'}),)

	class Meta:
		model = Employee
		fields = ['first_name', 'middle_name', 'last_name', 'emp_id', 'address', 'provincial_address', 'date_of_birth', 'date_hired', 'contract_expiration', 'gender', 'place_of_birth', 'civil_status', 'phone', 'company', 'gov_deductions_to_implement', 'sss_no', 'pagibig_no', 'sss_option', 'sss_bracket', 'sss_value', 'pagibig_value', 'philhealth_value', 'philhealth_no', 'tin_no', 'citizenship', 'remarks']
		


class PreferencesForm(forms.ModelForm):
	character_reference_name = forms.CharField(label='Nominee Name')
	character_reference_address = forms.CharField(label='Nominee Address')
	character_reference_phone = forms.CharField(label='Nominee Phone No.')

	class Meta:
		model = Employee_preferences
		exclude = ['employee']


class RecordsForm(forms.ModelForm):
	from_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
	to_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))

	class Meta:
		model = Employment_record
		exclude = ['employee']


class HiringDetailsForm(forms.ModelForm):
	PAYMENT_METHOD_CHOICES = CHOICES = (('', 'Choose method'),('weekly', 'Weekly'), ('semi-monthly', 'Semi-monthly'), ('monthly', 'Monthly'))
	payment_method = forms.CharField(widget=forms.Select(choices=PAYMENT_METHOD_CHOICES))
	BANK_CHOICES = CHOICES = (('', 'Choose bank'), ('ICICI', 'ICICI'), ('SBI', 'SBI'), ('HDFC', 'HDFC'),
							  ('axis', 'Axis'), ('Canara', 'Canara'), ('KVB', 'KVB'), ('others', 'others'),)
	bank = forms.CharField(label='Bank Name', widget=forms.Select(choices=BANK_CHOICES))
	rate = forms.DecimalField(label='Regular Pay')
	atm = forms.CharField(label='Account No.')
	overtime_formula = forms.CharField(label="Input overtime multiplier. (ex. 1.25)")

	class Meta:
		model = Employee_hiring_details
		exclude = ['employee']


class ResumeForm(forms.ModelForm):
	resume = forms.FileField(label='', help_text='')
	class Meta:
		model = Employee_resume
		exclude = ['employee']


class PictureForm(forms.ModelForm):
	picture = forms.FileField(label='', help_text='')

	class Meta:
		model = Employee_picture
		exclude = ['employee']


class CompanyLoanForm(forms.ModelForm):
	status = CHOICES = (('', 'Choose status'), ('Paid', 'Paid'), ('Not yet paid', 'Not Yet Paid'))
	status = forms.BooleanField(label="Paid", required=False)
	load_amount = forms.CharField(label="Loan Amount")
	class Meta:
		model = Employee_company_loan
		exclude = ['employee']


class PagibigLoanForm(forms.ModelForm):
	status = CHOICES = (('', 'Choose status'), ('Paid', 'Paid'), ('Not yet paid', 'Not Yet Paid'))
	status = forms.BooleanField(label="Paid", required=False)
	class Meta:
		model = Employee_pagibig_loan
		exclude = ['employee']


class UniformForm(forms.ModelForm):
	status = CHOICES = (('', 'Choose status'), ('Used', 'Used'), ('Not Used', 'Not Used'))
	status = forms.BooleanField(label="Used", required=False)
	class Meta:
		model = Employee_uniform
		exclude = ['employee']


class MedicalForm(forms.ModelForm):
	status = CHOICES = (('', 'Choose status'), ('Paid', 'Paid'), ('Not yet paid', 'Not Yet Paid'))
	status = forms.BooleanField(label="Paid", required=False)
	class Meta:
		exclude = ['employee']
		model = Employee_medical


class CanteenForm(forms.ModelForm):
	status = CHOICES = (('', 'Choose status'), ('Used', 'Used'), ('Not Used', 'Not Used'))
	status = forms.BooleanField(label="Used", required=False)

	class Meta:
		model = Employee_canteen
		exclude = ['employee']


class GatepassForm(forms.ModelForm):
	status = CHOICES = (('', 'Choose status'), ('Used', 'Used'), ('Not Used', 'Not Used'))
	status = forms.BooleanField(label="Used", required=False)
	class Meta:
		model = Employee_gatepass
		exclude = ['employee']


class ValeForm(forms.ModelForm):
	status = CHOICES = (('', 'Choose status'), ('Paid', 'Paid'), ('Not yet paid', 'Not Yet Paid'))
	status = forms.BooleanField(label="Paid", required=False)
	class Meta:
		model = Employee_vale
		exclude = ['employee']


class SearchForm(forms.ModelForm):
	company_name = forms.CharField(label='',
								   widget= forms.TextInput(attrs={'placeholder':'Company'}), required=False)

	class Meta:
		model = Company
		fields = ['company_name']


class EmployeeAcceptanceForm(forms.ModelForm):
	employment_status = CHOICES = (('', 'Choose status'),('Casual / Probationary', 'Casual / Probationary'), ('Seasonal', 'Seasonal'), ('Regular', 'Regular'))
	employment_status = forms.CharField(widget=forms.Select(choices=employment_status))
	start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
	end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
	class Meta:
		model = Employee_acceptance
		fields = ['employment_status', 'start_date', 'end_date', 'position', 'salary_per_day', 'salary_per_month']


class EmployeeLeaveHistory(forms.ModelForm):
	start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
	end_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
	class Meta:
		model = Employee_leave_history
		fields = ['start_date', 'end_date', 'no_of_days']


class UpdateRecord(forms.ModelForm):
	from_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
	to_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
	company = forms.CharField(label='Company Name')

	class Meta:
		model = Employment_record
		exclude = ['employee']


class Requirements(forms.ModelForm):
	nbi = forms.BooleanField(label="Pan Copy")
	barangay = forms.BooleanField(label="Aadhaar Card")
	medical = forms.BooleanField(label="Medical Report")
	sss_id = forms.BooleanField(label="PF Id")
	pagibig_id = forms.BooleanField(label="ESI Id")
	birth_certificate = forms.BooleanField(label="Birth Certificate")
	atm_application = forms.BooleanField(label="ATM Application Details")
	ph_id = forms.BooleanField(label="Health Insurance Id")
	hs_diploma = forms.BooleanField(label="Higher Secondary Certificate")
	college_diploma = forms.BooleanField(label="College Certificate")
	employee_contract = forms.BooleanField(label="Employee Contract")
	certificate_of_employment = forms.BooleanField(label="Certificate of Employment")
	photo = forms.BooleanField(label="Passport Size Photo")

	def __init__(self, *args, **kwargs):
		super(Requirements, self).__init__(*args, **kwargs)
		self.fields['nbi'].required = False
		self.fields['barangay'].required = False
		self.fields['medical'].required = False
		self.fields['sss_id'].required = False
		self.fields['pagibig_id'].required = False
		self.fields['birth_certificate'].required = False
		self.fields['atm_application'].required = False
		self.fields['ph_id'].required = False
		self.fields['hs_diploma'].required = False
		self.fields['college_diploma'].required = False
		self.fields['employee_contract'].required = False
		self.fields['certificate_of_employment'].required = False
		self.fields['photo'].required = False
		

	class Meta:
		model = Employee_requirements
		exclude = ['employee']


class MemoForm(forms.ModelForm):
	class Meta:
		model = Employee_memo
		exclude = ['employee']
