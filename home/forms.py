from django import forms

class Dateform(forms.Form):
	date = forms.DateField(label="",input_formats=['%d/%m/%Y'],widget= forms.TextInput(attrs={'placeholder':'31/12/2000'}))
	# widget = forms.SelectDateWidget

class Personform(forms.Form):
	last_name = 	forms.CharField(label="",max_length=100,required=False,widget= forms.TextInput(attrs={'placeholder':'Nom'}))
	first_name = 	forms.CharField(label="",max_length=100,required=False,widget= forms.TextInput(attrs={'placeholder':'Prénom'}))
	date = forms.DateField(label="",input_formats=['%d/%m/%Y'],required=False,widget= forms.TextInput(attrs={'placeholder':'31/12/2000'}))
	

class Personform2(forms.Form):
	last_name = 	forms.CharField(label="",max_length=100,required=False,widget= forms.TextInput(attrs={'placeholder':'Nom'}))
	first_name = 	forms.CharField(label="",max_length=100,required=False,widget= forms.TextInput(attrs={'placeholder':'Prénom'}))