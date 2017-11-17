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
    """
    request.session["card_id"] = 12
    request.session['user'] = request.user.username
    return render(request, 'carts/home.html')
