from django.urls import path
from base.views import index,live_search,product_detail, basket, add_to_cart ,PCV
from .views import index
urlpatterns = [
    path('', index, name='index'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path("create/", PCV.as_view(), name='create'),
    path("live_search/", live_search, name='live_search'),
    path("basket/", basket, name='basket'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart')

]

