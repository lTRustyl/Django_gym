from django.shortcuts import render
from django.views.generic import DetailView
from django.db.models import Q
from users.models import Users


def user_in_gum (request):
    user_count = Users.objects.filter(gum_status= True).count()
    return render(request, 'Gum/gums.html', {'user_count': user_count})