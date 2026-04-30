from django.shortcuts import render, redirect
from .models import FoodItem, Order, Wishlist
from django.contrib.auth.decorators import login_required
import random, requests


# MENU
def menu(request):
    items = FoodItem.objects.all()
    return render(request, 'app/menu.html', {'items': items})


# CART
def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart')


def cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for id, qty in cart.items():
        item = FoodItem.objects.get(id=id)
        item.qty = qty
        item.total = item.price * qty
        total += item.total
        items.append(item)

    return render(request, 'app/cart.html', {'items': items, 'total': total})


def remove_item(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
    request.session['cart'] = cart
    return redirect('cart')
def increase_qty(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)] += 1
    request.session['cart'] = cart
    return redirect('cart')


def decrease_qty(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)] -= 1
        if cart[str(id)] <= 0:
            del cart[str(id)]
    request.session['cart'] = cart
    return redirect('cart')


# CHECKOUT
def checkout(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for id, qty in cart.items():
        item = FoodItem.objects.get(id=id)
        item.qty = qty
        item.total = item.price * qty
        total += item.total
        items.append(item)

    if request.method == "POST":
        payment = request.POST.get('payment')
        time_slot = request.POST.get('time_slot')

        for item in items:
            Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                item=item,
                quantity=item.qty,
                total_price=item.total,
                payment_method=payment,
                time_slot=time_slot
            )

        request.session['cart'] = {}
        return render(request, 'app/success.html', {'total': total})

    return render(request, 'app/checkout.html', {'items': items, 'total': total})


# WISHLIST
@login_required
def add_to_wishlist(request, id):
    item = FoodItem.objects.get(id=id)
    Wishlist.objects.get_or_create(user=request.user, item=item)
    return redirect('wishlist')


@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'app/wishlist.html', {'items': items})


# OTP LOGIN
def login(request):
    if request.method == "POST":
        phone = request.POST.get('phone')

        otp = random.randint(1000, 9999)
        request.session['otp'] = str(otp)

        #API KEY
        url = "https://www.fast2sms.com/dev/bulkV2"
        payload = {
            "route": "otp",
            "variables_values": otp,
            "numbers": "91" + phone,
        }
        headers = {
            "authorization": "YOUR_API_KEY",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        try:
            requests.post(url, data=payload, headers=headers)
        except:
            print("SMS Failed")

        return redirect('verify_otp')

    return render(request, 'app/login.html')


def verify_otp(request):
    if request.method == "POST":
        if request.POST.get('otp') == request.session.get('otp'):
            return redirect('menu')

    return render(request, 'app/verify_otp.html')