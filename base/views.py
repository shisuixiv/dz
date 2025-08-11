from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from base.models import Product
from base.forms import ProductForm
from django.http import JsonResponse
from .filters import PF
from django.template.loader import render_to_string

# Главная страница с фильтром
def index(request):
    products = Product.objects.all()
    product_filter = PF(request.GET, queryset=products)
    # Сразу выводим все товары (product_filter.qs учитывает фильтр)
    return render(request, 'index.html', {
        'product_filter': product_filter,
        'products': product_filter.qs  # для начальной загрузки
    })

# Детальная страница товара
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

# Создание товара
class PCV(CreateView):
    template_name = 'create.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('index')

# AJAX-фильтр (поиск + цена)
def live_search(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    
    if query:
        products = products.filter(title__icontains=query)
        
    price_gte = request.GET.get('price_gte')
    price_lte = request.GET.get('price_lte')

    if price_gte:
        products = products.filter(price__gte=price_gte)
    if price_lte:
        products = products.filter(price__lte=price_lte)

    

    html = render_to_string('product_cards.html', {'products': products})
    return JsonResponse({'html': html})


def basket(request):
    cart = request.session.get('cart', {})
    cart_items = []

    total = 0
    for product_id, item in cart.items():
        item_total = item['price'] * item['quantity']
        total += item_total
        cart_items.append({
            'title': item['title'],
            'price': item['price'],
            'quantity': item['quantity'],
            'total_price': item_total,
        })

    return render(request, 'basket.html', {
        'cart_items': cart_items,
        'total_price': total
    })


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = request.session.get('cart', {})

    product_id = str(id)
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'title': product.title,
            'price': float(product.price),
            'quantity': 1,
        }

    request.session['cart'] = cart
    return redirect('basket')

