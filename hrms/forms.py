from django import forms
from django.contrib.auth.models import User
from .models import Company, Company_rates

class CompanyAddForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['company_name', 'contact_person', 'phone', 'fax', 'email']

class CompanyRates(forms.ModelForm):
	class Meta:
		model = Company_rates
		fields = ['base_rate', 'activate_rates', 'base_training_rate', 'activate_training_rate']


class CompanyGovDeduct(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CompanyGovDeduct, self).__init__(*args, **kwargs)
		self.fields['pagibig'].required = False

	class Meta:
	 	model = Company_rates
	 	fields = ['sss', 'philhealth', 'pagibig']
	 	labels = {
	 		'sss':'PF',
	 		'philhealth':'ESI',
			'pagibig': 'Housing Loan',
	 	}



class CompanyOtherOptions(forms.ModelForm):
	ecola_rate = forms.DecimalField(label="Set Company Training Rate", required="False")
	activate_ecola = forms.BooleanField(label="Activate Training Rate", required="False")
	activate_overtime = forms.BooleanField(label="Activate Overtime Allowance", required="False")
	activate_1_25_overtime = forms.BooleanField(label="Activate ExtraShift Allowance")
	activate_rest_day = forms.BooleanField(label="Activate Rest Day")
	activate_holiday = forms.BooleanField(label="Activate Holidays")
	activate_sunday = forms.BooleanField(label="Activate Sundays")
	activate_night_differential = forms.BooleanField(label="Activate Night Allowance")
	activate_service_fee = forms.BooleanField(label="Activate Service Fee")
	activate_tshirt = forms.BooleanField(label="Activate Employee Tshirt")
	activate_pants = forms.BooleanField(label="Activate Employee Bottoms")
	activate_house = forms.BooleanField(label="Activate House Rent")
	activate_gatepass = forms.BooleanField(label="Activate Gatepass")
	activate_medical = forms.BooleanField(label="Activate Medical Support")
	activate_vale = forms.BooleanField(label="Activate Cash Advance")
	activate_uniform = forms.BooleanField(label="Activate Employee Uniform")
	activate_company_loan = forms.BooleanField(label="Activate Company Loan")
	activate_pagibig_loan = forms.BooleanField(label="Activate PF Amount")
	activate_sss_loan = forms.BooleanField(label="Activate ESI Loan")
	activate_canteen = forms.BooleanField(label="Activate Canteen Service")
	activate_allowance = forms.BooleanField(label="Activate Special Allowance")
	activate_transpo_allowance = forms.BooleanField(label="Activate Transport Allowance")
	activate_special = forms.BooleanField(label="Activate Special Holidays")
	activate_adjustment = forms.BooleanField(label="Activate Daily Pay")
	activate_thirteenth_month = forms.BooleanField(label="Activate Weekly Pay")
	activate_tardiness = forms.BooleanField(label="Activate Tardiness")
	activate_sil = forms.BooleanField(label="Activate Accomodation")
	activate_rf = forms.BooleanField(label="Activate Half Shift")
	activate_misc = forms.BooleanField(label="Activate Vouchers")

	def __init__(self, *args, **kwargs):
		super(CompanyOtherOptions, self).__init__(*args, **kwargs)
		self.fields['ecola_rate'].required = False
		self.fields['activate_ecola'].required = False
		self.fields['activate_overtime'].required = False
		self.fields['activate_1_25_overtime'].required = False
		self.fields['activate_holiday'].required = False
		self.fields['activate_rest_day'].required = False
		self.fields['activate_special'].required = False
		self.fields['activate_night_differential'].required = False
		self.fields['activate_thirteenth_month'].required = False
		self.fields['activate_sil'].required = False
		self.fields['activate_tshirt'].required = False
		self.fields['activate_rf'].required = False
		self.fields['activate_house'].required = False
		self.fields['activate_misc'].required = False
		self.fields['activate_gatepass'].required = False
		self.fields['activate_medical'].required = False
		self.fields['activate_pants'].required = False
		self.fields['activate_vale'].required = False
		self.fields['activate_uniform'].required = False
		self.fields['activate_company_loan'].required = False
		self.fields['activate_pagibig_loan'].required = False
		self.fields['activate_sss_loan'].required = False
		self.fields['activate_canteen'].required = False
		self.fields['activate_service_fee'].required = False
		self.fields['activate_sunday'].required = False
		self.fields['activate_tardiness'].required = False
		self.fields['activate_allowance'].required = False
		self.fields['activate_adjustment'].required = False
		self.fields['activate_transpo_allowance'].required = False


	class Meta:
		model = Company_rates
		fields = ['ecola_rate','activate_ecola', 'activate_overtime', 'activate_1_25_overtime',
				  'activate_holiday','activate_rest_day', 'activate_special',
				 'activate_night_differential', 'activate_thirteenth_month',
				'activate_sil', 'activate_tshirt', 'activate_rf', 'activate_house',
				  'activate_misc','activate_gatepass', 'activate_medical' , 'activate_pants',
				'activate_vale', 'activate_uniform' , 'activate_company_loan', 'activate_pagibig_loan' ,
				  'activate_sss_loan', 'activate_canteen', 'activate_service_fee',
				'activate_sunday', 'activate_tardiness', 'activate_allowance', 'activate_adjustment',
				  'activate_transpo_allowance'
		]
