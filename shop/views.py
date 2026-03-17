from django.shortcuts import render
from django.views.generic import DetailView
from django.db.models import Q
from .models import Prods


def prods_page(request):
    search_query = request.GET.get('search', '')
    if search_query:
        prods = Prods.objects.filter(Q(name_prod__icontains=search_query) | Q(brand__icontains=search_query))
    else:
        prods = Prods.objects.order_by("-date")
    return render(request, 'shop/prods.html', {'prods': prods})


class ProdsDetailView(DetailView):
    model = Prods
    template_name = 'shop/prod.html'
    context_object_name = 'prods'

