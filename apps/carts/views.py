from django.shortcuts import render


# Create your views here.


def cart_home(request):
    """
        print('cat====================== ')
        print(request.session) # on the request
        print(dir(request.session))
        request.session.set_expiry(300) # 5 minutes
        key = request.session.session_key
        print(key)
        print('cat====================== ')
        request.session["card_id"] = 12
        request.session['user'] = request.user.username
    """
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:  # and isinstance(cart_id, int):
        print('create new cart')
        request.session['cart_id'] = 12
    else:
        print('Cart ID exists')
    return render(request, 'carts/home.html')
