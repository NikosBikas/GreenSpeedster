from django.shortcuts import render
from store.models import Product, ReviewRating ,Slider

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    sliderdata = Slider.objects.all()

    #Get the Reviews
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)


    context = {
        'products': products, 
        'reviews': reviews,
        'slider': sliderdata,
    }
    return render(request,'home.html', context)

