from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
	
	context={}
	return render(request, 'core/index.html',context)
	
class AboutView(TemplateView):
	template_name = 'core/about.html'