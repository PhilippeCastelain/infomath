#from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Theme, Cours, Td


class HomeView(TemplateView):
	template_name = 'nsi/home.html'

class ThemeListView(ListView):
	model = Theme
	template_name = 'nsi/themes.html' 
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context['par_niveau_list'] = [('Première',Theme.objects.filter(niveau='P')),
									  ('Terminale',Theme.objects.filter(niveau='T')),
									  ('Approfondissement',Theme.objects.filter(niveau='A'))]
		return context

class ThemeNiveauListView(ListView):
	context_object_name = 'list_theme'
	template_name = 'nsi/themes_niveau.html'
	level = {'A':'Approfondissement', 'P':'Première', 'T':'Terminale'}
	def get_queryset(self):
		return Theme.objects.filter(niveau=self.kwargs['niveau']) 

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super().get_context_data(**kwargs)
		context['niveau'] = self.level[self.kwargs['niveau']]
		return context

class ThemeDetailView(DetailView):
	model = Theme
	template_name = 'nsi/theme_detail.html'

class CoursDetailView(DetailView):
	model = Cours
	template_name = 'nsi/cours_detail.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['image1'] = context['cours'].theme.code + '/' + context['cours'].image1
		context['image2'] = context['cours'].theme.code + '/' + context['cours'].image2
		context['image3'] = context['cours'].theme.code + '/' + context['cours'].image3
		return context

#class TdDetailView(DetailView):
#	model = Td
#	template_name = 'nsi/td_detail.html'
