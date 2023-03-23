from django.shortcuts import render
from .models import Book

from django.views.generic import DetailView


# Home views
default_layout = 'agency'
default_header = 'dark'
default_header_image = '/unice/djbooks/static/assets/images/logo/5.png'
header_logos = {
    "black_logo":'/unice/djbooks/static/assets/images/logo/5.png',
    "white_logo": '/unice/djbooks/static/assets/images/logo/1.png',
    "pink_logo": '/unice/djbooks/static/assets/images/logo/3.png',
}


# custom views

class BookDetailView(DetailView):
    model = Book
    template_name = "shop/product-pages/product-page(3-col-left)/product-page(3-col-left).html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add data for the context
        data = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
        context.update(data)
        return context

def index(request):
    context={
        "header_logo":default_header_image,
        'books': Book.objects.all(),
        'header_classes':'ecommerce nav-fix','header_image':header_logos["black_logo"]}
    return render(request,'home/ecommerce_layout/ecommerce_layout.html',context)

# pages views 
from allauth.account.views import LoginView
class BotLoginView(LoginView):

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add data for the context
        data = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
        context.update(data)
        return context

def pages_404(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":default_header}
    return render(request,'pages/404/404.html',context)

def faqs(request):
    context={"header_logo":default_header_image,"header":"dark","layout":"agency"}
    return render(request,'pages/faq/faq.html',context)

def collection(request):
    context={"header_logo":default_header_image,"header":"dark","layout":"agency"}
    return render(request,'pages/collection/collection.html',context)

def typography(request):
    context={"header_logo":default_header_image,"header":"dark","layout":"agency"}
    return render(request,'pages/typography/typography.html',context)

def maintenance(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":default_header}
    return render(request,'pages/maintenance/maintenance.html',context)

def about_us(request):
    context={"header_logo":default_header_image,"header":"dark","layout":"agency"} 
    return render(request,'pages/about-us/about-us.html',context)


# shop views

    # shop categories views:

def shop_categories_left_sidebar(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-leftsidebar(4-grid)/category-page-leftsidebar(4-grid).html',context)

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
    return render(request,'shop/shop-categories/category-page-nosidebar(2-grid)/category-page-nosidebar(2-grid).html',context)

def shop_categories_no_sidebar_3(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-nosidebar(3-grid)/category-page-nosidebar(3-grid).html',context)

def shop_categories_no_sidebar_6(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page-nosidebar(6-grid)/category-page-nosidebar(6-grid).html',context)

def shop_categories_metro(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-categories/category-page(metro)/category-page(metro).html',context)

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

def books(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/product-pages/product-page(3-col-left)/product-page(3-col-left).html',context)

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

def shop_pages_cart(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative"}
    return render(request,'shop/shop-pages/cart/cart.html',context)

def shop_pages_checkout(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-pages/checkout/checkout.html',context)

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
    context = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
    return render(request,'shop/shop-pages/wishlist/wishlist.html',context)

# features views

    # footer options views

def features_footer_default(request):
    context = {"header_logo":default_header_image,"header":"dark","layout":"","parent":"Footer Default","child":"Footer Style"}
    return render(request,'features/footer-options/footer-default/footer-default.html',context)
