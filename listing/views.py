from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from listing.choice import state_choices,price_choices,bedroom_choices
# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context={
        'listings':paged_listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
        }
    return render(request, 'listing/listings.html',context)






def listing(request,listing_id):
    listing=Listing.objects.get(id=listing_id)
    
    context={
        'listing': listing
        
    }
    
    return render(request, 'listing/listing.html',context)



def search(request):
    queryset_list=Listing.objects.order_by('-list_date')
    
    #keyword
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=Listing.objects.filter(discription__icontains=keywords)
    
    
    #city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=Listing.objects.filter(city__iexact=city) 
            
            
            
    #state
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            queryset_list=Listing.objects.filter(state__iexact=state) 
            
            
            
     #bedroom
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            queryset_list=Listing.objects.filter(bedrooms__lte=bedrooms) 
            
            
     #price
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            queryset_list=Listing.objects.filter(price__lte=price) 
        
        
        
    
        
    context={
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'value':request.GET
    }
    return render(request, 'listing/search.html',context)

