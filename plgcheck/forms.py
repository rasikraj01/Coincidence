from django import forms

class CheckForm(forms.Form):
	 cnt1 = forms.CharField(label='Enter Source Code 1', widget=forms.Textarea)
	 cnt2 = forms.CharField(label='Enter Source Code 2', widget=forms.Textarea)