from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import Contacts, Product, Billing_detail, Order, Feedback

# Create your views here.
def base(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    return render(request, 'base.html', {'all_products_count':all_products_count})




def index(request):
    feedbacks = Feedback.objects.all()
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    products = Product.objects.all()[:6]
    productss = Product.objects.all()[::-1]

    return render(request, 'index.html', {'products':products, 'productss':productss, 'all_products_count':all_products_count, 'feedbacks':feedbacks})

def products(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    products = Product.objects.all()
    return render(request, 'shop.html', {'products':products, 'all_products_count':all_products_count})


def about_us(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    return render(request, 'about.html', {'all_products_count':all_products_count})


def contacts(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    return render(request, 'contact.html', {'all_products_count':all_products_count})


def shop_single(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    return render(request, 'shop-single.html', {'all_products_count':all_products_count})



def sendContact(request):
    if request.method == 'POST':
        contact = Contacts()
        contact.first_name = request.POST.get('c_fname')
        contact.last_name = request.POST.get('c_lname')
        contact.email = request.POST.get('c_email')
        contact.message = request.POST.get('c_message')
        contact.save()

        return HttpResponseRedirect('/contacts')



def product(request, pk):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    product = Product.objects.get(pk=pk)
    return render(request, 'shop-single.html', {'product':product, 'all_products_count':all_products_count})
    


def addToCart(request, pk):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(pk)
    request.session['cart_session'] = cart_session
 
    return HttpResponseRedirect('/cart')



def cart(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    products_cart = Product.objects.filter(pk__in=cart_session)

    all_products_total_sum = 0
    for product_cart in products_cart:
        product_cart.count = cart_session.count(product_cart.id)
        product_cart.sum = product_cart.count * product_cart.price
        all_products_total_sum += product_cart.sum


    return render(request, 'cart.html', {'products_cart':products_cart, 'cart_session':cart_session,
                                         'all_products_count':all_products_count,
                                         'all_products_total_sum':all_products_total_sum})



        
        
def update_cart(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    request.session['cart_session'] = []
    return render(request, 'cart.html', {'all_products_count':all_products_count})


def del_product(request, pk):
    cart_session = request.session.get('cart_session', [])
    cart_session.remove(pk)
    request.session['cart_session'] = cart_session
    return HttpResponseRedirect('/cart')


def checkout(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    products_cart = Product.objects.filter(pk__in=cart_session)
   

    all_products_total_sum = 0
    for product_cart in products_cart:
        product_cart.count = cart_session.count(product_cart.id)
        product_cart.sum = product_cart.count * product_cart.price
        all_products_total_sum += product_cart.sum


    return render(request, 'checkout.html', {'products_cart':products_cart, 'cart_session':cart_session,
                                         'all_products_count':all_products_count,
                                         'all_products_total_sum':all_products_total_sum})




def addOrder(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    products_cart = Product.objects.filter(pk__in=cart_session)
   

    all_products_total_sum = 0
    for product_cart in products_cart:
        product_cart.count = cart_session.count(product_cart.id)
        product_cart.sum = product_cart.count * product_cart.price
        all_products_total_sum += product_cart.sum

    if request.method == 'POST':
        detail_billing = Billing_detail()
        detail_billing.first_name = request.POST.get('c_fname')
        detail_billing.last_name = request.POST.get('c_lname')
        detail_billing.email = request.POST.get('c_email_address')
        detail_billing.number = request.POST.get('c_phone')
        detail_billing.note_message = request.POST.get('c_order_notes')
        detail_billing.country = request.POST.get('c_country')
        detail_billing.city = request.POST.get('c_city')
        detail_billing.street = request.POST.get('c_street')
        detail_billing.posta_zip = request.POST.get('c_postal_zip')
        detail_billing.save()

        for item in products_cart:
            order = Order()
            order.product = item.name
            order.p_price = item.price
            order.p_count = item.count
            order.p_total = item.sum
            order.customer = detail_billing
            order.save()
    cart_session = request.session.get('cart_session', [])
    cart_session.clear()
    request.session['cart_session'] = cart_session
    all_products_count = len(cart_session)

    
    return render(request, 'thankyou.html', {'all_products_count':all_products_count})


def search(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)
    if request.method == 'POST':
        search = request.POST.get('search')
        search_pr = Product.objects.filter(name__icontains=search)

        return render(request, 'searched-pr.html', {'search_pr':search_pr, 'len_pr':len(search_pr),
        'all_products_count':all_products_count})



def author(request):
    cart_session = request.session.get('cart_session', [])
    all_products_count = len(cart_session)

    return render(request, 'author.html', {'all_products_count':all_products_count})