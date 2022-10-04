from django.urls import path
from . import views


urlpatterns = [
    path('',views.store, name='store'),
    path('category/<slug:category_slug>', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'), 
    path('search/',views.search, name='search'),
    path('search_price/',views.search_price, name='search_price'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    path('terms/', views.terms, name = 'terms'),
    path('about_us/',views.about_us, name='about_us'),
    path('service/',views.service, name='service'),
    path('returns_refunds/',views.returns_refunds, name='returns_refunds'),
    path('contact/',views.contact, name='contact'),


    
]
