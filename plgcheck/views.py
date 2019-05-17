from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .forms import CheckForm
from .Ld_similarity import Ld_similarity

class IndexView(TemplateView):
	form_class = CheckForm
	template_name = "index.html"

	# print(Ld_similarity('this','was'))
	def get(self, request, *args, **kwrgs):
		form = self.form_class()
		return render(request, self.template_name , {'form': form})
	
	def post(self, request, *args, **kwrgs):
		form = self.form_class(request.POST)
		# if form.is_valid() and (len(str(form.cleaned_data['cnt1'])) <= 10000 or len(str(form.cleaned_data['cnt2'])) <= 10000):
		# 		sim = Ld_similarity(str(form.cleaned_data['cnt1']), str(form.cleaned_data['cnt2']))
		# 		return render(request, self.template_name , {'form': form, 'sim' : sim})

		return render(request, self.template_name , {'form': form})