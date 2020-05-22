from django.shortcuts import render
from .models import Portfolio

# Create your views here.


def home(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/home.html', {'portfolios': portfolios})
