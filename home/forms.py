from django import forms

class Dateform(forms.Form):
	date = forms.DateField(label="",input_formats=['%d/%m/%Y'],initial='31/12/2000')
	# widget = forms.SelectDateWidget

class Personform(forms.Form):
	last_name = forms.CharField(label="",initial='nom')
	first_name = forms.CharField(label="",initial='prénom')
	date = forms.DateField(label="",input_formats=['%d/%m/%Y'],initial='31/12/2000')
	

class Personform2(forms.Form):
	last_name = forms.CharField(label="",initial='nom')
	first_name = forms.CharField(label="",initial='prénom')