from django.shortcuts import render
from . import models
from django.views.generic import (TemplateView, ListView, DetailView,
								CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
	template_name = 'Home.html'

class ProductListView(ListView):
	model = models.Product

class ProductDetailView(DetailView):
	model = models.Product

class ProductCreateView(CreateView):
	fields = '__all__'
	model = models.Product

class ProductUpdateView(UpdateView):
	fields = ['Name', 'Company', 'Price']
	model = models.Product

class ProductDeleteView(DeleteView):
	model = models.Product
	success_url = reverse_lazy('basic_app:product_list')