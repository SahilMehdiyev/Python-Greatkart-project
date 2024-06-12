from django.shortcuts import render,redirect,HttpResponse
from store.models import Product
from .models import Cart,CartItem


def _cart_id(request):
    # Kullanıcının oturum anahtarını alır
    cart = request.session.session_key
    if not cart:
        # Eğer oturum anahtarı yoksa yeni bir oturum oluşturur
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    # Belirtilen product_id ile ürünü veritabanından alır
    product = Product.objects.get(id=product_id)
    
    try:
        # Mevcut oturum anahtarına sahip sepeti almaya çalışır
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        # Eğer böyle bir sepet yoksa yeni bir sepet oluşturur
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )    
    cart.save()
    
    try:
        # Belirtilen ürün ve sepet ile eşleşen bir sepet öğesini almaya çalışır
        cart_item = CartItem.objects.get(product=product, cart=cart)
        # Eğer böyle bir öğe varsa miktarını bir artırır
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        # Eğer böyle bir öğe yoksa yeni bir sepet öğesi oluşturur
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
        )    
        cart_item.save()
        
    return HttpResponse(cart_item.quantity)  
    exit()      

    # İşlem tamamlandıktan sonra kullanıcının sepet sayfasına yönlendirilmesini sağlar
    return redirect('cart')



def cart(request):
    
    return render(request, 'store/cart.html')