from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# untuk tampilan home (menggunakan class base view)
class TemplatePage(TemplateView):
	# template berada di homeapp
	template_name = 'index.html'

	def get(self, request, *arg, **kwargs):
		return render(request,self.template_name,{'heading':'Sumber'})