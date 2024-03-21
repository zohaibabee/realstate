from django.shortcuts import render
from django.http import HttpResponse
from listing.models import Listing
from retalor.models import Realtor
from listing.choice import state_choices,bedroom_choices,price_choices
# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
                     }
    return render(request, 'pages/index.html',context)





def about(request):
    realtors=Realtor.objects.order_by('-hire_date')
    
    realtor_mvp=Realtor.objects.filter(is_mvp=True)  
    context={
        'realtors':realtors,
        'realtor_mvp':realtor_mvp
    }
    return render(request, 'pages/about.html',context)


