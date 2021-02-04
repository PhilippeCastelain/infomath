from django.urls import path
from . import views

app_name = 'nsi'
urlpatterns = [
	path('',views.HomeView.as_view(), name='home'),
	path('themes/', views.ThemeListView.as_view(), name='themes'),
	path('themes/<int:pk>/', views.ThemeDetailView.as_view(), name='theme-detail'),
	path('themes/<niveau>/', views.ThemeNiveauListView.as_view(), name='themes-niveau'),
	path('cours/<int:pk>/', views.CoursDetailView.as_view(), name='cours-detail'),
]