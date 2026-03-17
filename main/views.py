from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from shop.models import Prods

def main_page(request):
	prods = Prods.objects.order_by("-date")[:8]
	return render(request, 'Main/main.html', {'prods': prods})
