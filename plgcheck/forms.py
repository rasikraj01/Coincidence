from django import forms

class CheckForm(forms.Form):
	 cnt1 = forms.CharField(label='Enter Source Code 1')
	 cnt2 = forms.CharField(label='Enter Source Code 2')