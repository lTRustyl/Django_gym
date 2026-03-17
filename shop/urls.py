from django.urls import path
from . import views

urlpatterns = [
    path('',views.prods_page, name="prods_page_url" ),
    path('<int:pk>', views.ProdsDetailView.as_view(), name = 'prods-detail')
]