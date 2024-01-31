from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('products/', views.products, name='products'),
	path('activities/', views.activities, name='activities'),
	path('aboutus/', views.aboutus, name='aboutus'),
	path('clients/', views.clients, name='clients'),
	path('client/', views.client, name='client'),
	path('energy/', views.energy, name='energy'),
	path('marketing/', views.marketing, name='marketing'),
	path('catering/', views.catering, name='catering'),
	path('constructing/', views.constructing, name='constructing'),
]