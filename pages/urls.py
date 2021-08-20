from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name= 'about'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('shop/', shop, name='shop'),
    path('elements/', elements, name='elements'),
    path('portfolio-item/', portfolio_item, name='portfolio-item'),
    path('blog-single/', blog_single, name='blog-single'),
    path('shop-single/', shop_single, name='shop-single'),
    path('portfolio-category/', portfolio_category, name='portfolio-category'),
    
]