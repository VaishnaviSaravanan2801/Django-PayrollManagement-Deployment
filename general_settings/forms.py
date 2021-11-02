from django import forms
from .models import General_settings, BracketSSContribEE

class GeneralInfoForm(forms.ModelForm):
	class Meta:
		model = General_settings
		fields = ['main_company', 'template_name', 'company_address', 'company_contacts']


class BracketSSContribEEForm(forms.ModelForm):
	contrib_amount = forms.DecimalField(label="Contribution Amount")
	ranged = forms.CharField(label="Salary Ranged")

	class Meta:
		model = BracketSSContribEE
		fields = ['contrib_amount', 'ranged']