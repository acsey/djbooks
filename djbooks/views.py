from django.utils import timezone
from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Book, OrderBook, Order, Address
from .forms import CheckoutForm, SearchForm

from django.views.generic import DetailView, View


# Home views
default_layout = 'agency'
default_header = 'dark'
# TODO: remove absolute path
# default_header_image = '/static/assets/images/logo/logo2.jpg' 
default_header_image = '/static/assets/images/logo/logo-transparent.png'


# custom views

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = "shop/product-pages/product-page(3-col-left)/product-page(3-col-left).html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add data for the context
        data = {"layout":default_layout,"header":"dark position-relative nav-lg"}
        context.update(data)
        return context
    
# class BookSearchView(View):
#     model = Book
from django.db.models import Q

def search_view(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        # Perform search operation using the query
        # You can use Django ORM or any other method to fetch the search results
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(tags__name__in=[query])
        )

    return render(request, 'search-book.html', {'form': form, 'results': results, "layout":default_layout,"header":"dark position-relative nav-lg"})

def index(request):
    context={
        
        'books': Book.objects.all(),
        'new_books': Book.objects.all().order_by('-id')[:5],
        'header_classes':'ecommerce nav-fix','header_image':default_header_image}
    return render(request,'home/ecommerce_layout/ecommerce_layout.html',context)

def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class CheckoutView(View):
    
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'order': order,
                
                "layout":default_layout,
                "header":"dark position-relative nav-lg"
            }

            shipping_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='S',
                default=True
            )
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]})

            billing_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='B',
                default=True
            )
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]})
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("djbooks:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)

            if form.is_valid():
                save_address = form.cleaned_data.get(
                    'save_address')
                if save_address:
                    street_address = form.cleaned_data.get(
                        'street_address')
                    shipping_country = form.cleaned_data.get(
                        'shipping_country') or "México"
                    shipping_city = form.cleaned_data.get(
                        'shipping_city')
                    shipping_zip = form.cleaned_data.get('shipping_zip')

                    if is_valid_form([street_address, shipping_country, shipping_zip, shipping_city]):
                        shipping_address = Address(
                            user=self.request.user,
                            names=form.cleaned_data.get('names'),
                            last_names=form.cleaned_data.get('last_names'),
                            phone=form.cleaned_data.get('phone'),
                            email=form.cleaned_data.get('email'),
                            street_address=street_address,
                            shipping_country=shipping_country,
                            shipping_city=shipping_city,
                            shipping_zip=shipping_zip,
                            address_type='S'
                        )

                        order.shipping_address = shipping_address

                        shipping_option = form.cleaned_data.get('shipping_option')
                        order.shipping_option = shipping_option

                        set_default_shipping = form.cleaned_data.get(
                            'set_default_shipping')
                        if set_default_shipping:
                            #TODO: Use this for autofill
                            shipping_address.default = True
                        shipping_address.save()
                        order.save()
                        

                    else:
                        messages.warning(
                            self.request, "Please fill in the required shipping address fields")
                        
                payment_option = form.cleaned_data.get('payment_option')
                shipping_option = form.cleaned_data.get('shipping_option')

                from json import dumps #TODO: REMOOOOVE

                print("FORM: ", dumps(form.cleaned_data, indent=4))
                print("Ship: ", shipping_option)

                if payment_option == 'mercado_pago':
                    return redirect('djbooks:payment' )#,kwargs={'payment_option':'mercado_pago'})
                elif payment_option == 'paypal':
                    messages.info(self.request, "Pago con Paypal")
                    return redirect('djbooks:checkout')
                    #return redirect('djbooks:payment', payment_option='paypal')
                else:
                    messages.warning(self.request, "Invalid payment option selected")
                    return redirect('djbooks:checkout')
            else:
                messages.warning(self.request, f"Form is not valid {form.errors.as_text()}")
                return redirect('djbooks:checkout')

        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("djbooks:order-summary")


class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        # if order.billing_address:
        #     messages.info(self.request, "Agregaste una dirección")
        # else:
        #     messages.warning(self.request, "No agregaste una dirección")
        #     return redirect("core:checkout")
        context = {
            'order': order,
        }
        data = {"layout":default_layout,"header":"dark position-relative nav-lg"}
        context.update(data)
        return render(self.request, "payment.html", context)





from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

class PaymentSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            data = {"layout":default_layout,"header":"dark position-relative nav-lg"}
            context.update(data)
            return render(self.request, 'purchases.html',context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Tu carrito está vacío")
            return redirect("/")


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            data = {"layout":default_layout,"header":"dark position-relative nav-lg"}
            context.update(data)
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "Tu carrito está vacío")
            return redirect("/")


# pages views 
from allauth.account.views import LoginView, SignupView
class CustomLoginView(LoginView):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add data for the context
        data = {"layout":default_layout,"header":"dark position-relative nav-lg"}
        context.update(data)
        return context

class CustomSignupView(SignupView):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add data for the context
        data = {"layout":default_layout,"header":"dark position-relative nav-lg"}
        context.update(data)
        return context

def pages_404(request):
    context = {"layout":default_layout,"header":default_header}
    return render(request,'pages/404/404.html',context)

def faqs(request):
    context={"header":"dark","layout":"agency"}
    return render(request,'pages/faq/faq.html',context)

def collection(request):
    context={
        
        "header":"dark",
        "layout":"agency", 
        # passing a dict with the total of books per category
        "data": Book.get_book_all_categories_count()
    }
    return render(request,'pages/collection/collection.html',context)

# cart views

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_item, created = OrderBook.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Libro agregado al carrito.")
            return redirect("djbooks:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("djbooks:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("djbooks:order-summary")


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderBook.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "Libro retirado del carrito")
            return redirect("djbooks:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("djbooks:order-summary")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("djbooks:order-summary")

@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderBook.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "Libro retirado del carrito")
            return redirect("djbooks:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("djbooks:order-summary")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("djbooks:order-summary")

def books(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(3-col-left)/product-page(3-col-left).html',context)

# shop views

    # shop categories views:

def shop_categories_left_sidebar(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'pages/typography/typography.html',context)

def shop_categories_two_sidebar(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-categories/category-page-leftsidebar(2-grid)/category-page-leftsidebar(2-grid).html',context)

def shop_categories_three_sidebar(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-categories/category-page-leftsidebar(3-grid)/category-page-leftsidebar(3-grid).html',context)

def shop_categories_six_sidebar(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-categories/category-page-leftsidebar(6-grid)/category-page-leftsidebar(6-grid).html',context)

def shop_categories_right_sidebar(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-rightsidebar(4-grid)/category-page-rightsidebar(4-grid).html',context)

def shop_categories_right_2_grid(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-rightsidebar(2-grid)/category-page-rightsidebar(2-grid).html',context)

def shop_categories_right_3_grid(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-rightsidebar(3-grid)/category-page-rightsidebar(3-grid).html',context)

def shop_categories_right_6_grid(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-rightsidebar(6-grid)/category-page-rightsidebar(6-grid).html',context)

def shop_categories_no_sidebar(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-nosidebar(4-grid)/category-page-nosidebar(4-grid).html',context)

def shop_categories_no_sidebar_2(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-nosidebar(6-grid)/category-page-nosidebar(pe).html',context)

def shop_categories_no_sidebar_3(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-nosidebar(6-grid)/category-page-nosidebar(lf).html',context)

def shop_categories_no_sidebar_6(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-nosidebar(6-grid)/category-page-nosidebar(6-grid).html',context)

def request_book(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'blog/blog-details/blog-detail/components/blog-main.html',context)

    # product pages views

def shop_product_no_sidebar(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(no-sidebar)/product-page(no-sidebar).html',context)

def shop_product_left_sidebar(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(left-sidebar)/product-page(left-sidebar).html',context)

def shop_product_right_sidebar(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark nav-lg"}
    return render(request,'shop/product-pages/product-page(right-sidebar)/product-page(right-sidebar).html',context)

def shop_product_3_grid(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(3-column)/product-page(3-column).html',context)


def shop_product_3_grid_right(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(3-col-right)/product-page(3-col-right).html',context)

def shop_product_accordian(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(accordian)/product-page(accordian).html',context)

def shop_product_bundle(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(bundle)/product-page(bundle).html',context)

def shop_product_image_swatch(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(image-swatch)/product-page(image-swatch).html',context)

def shop_product_image_outside(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(image-outside)/product-page(image-outside).html',context)

def shop_product_image_sticky(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark nav-lg"}
    return render(request,'shop/product-pages/product-page(sticky)/product-page(sticky).html',context)

    # shop pages views

def shop_pages_compare(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-pages/compare/compare.html',context)

def shop_pages_compare_2(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-pages/compare-2/compare-2.html',context)

def shop_pages_signup(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-pages/signup/signup.html',context)

def shop_pages_login(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-pages/login/login.html',context)

def shop_pages_wishlist(request):
    context = {"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-pages/wishlist/wishlist.html',context)
