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

def products(request):
    context = {
        'books': Book.objects.all()
    }
    print(context)
    return render(request, "products.html", context)

class BookDetailView(DetailView):
    model = Book
    template_name = "shop/product-pages/product-page(3-col-left)/product-page(3-col-left).html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        extra_headers = {"header_logo":default_header_image,"layout":default_layout,"header":"dark position-relative nav-lg"}
        context.update(extra_headers)
        return context

def index(request):
    context={
        "header_logo":default_header_image,
        'books': Book.objects.all(),
        'header_classes':'ecommerce nav-fix','header_image':header_logos["black_logo"]}
    return render(request,'home/ecommerce_layout/ecommerce_layout.html',context)

# pages views 

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

    # team pages views
def team(request):
    context={"header_logo":default_header_image,"header":"dark","layout":"agency"} 
    return render(request,'pages/team/team/team.html',context)

def team_grid(request):
    context={"header_logo":default_header_image,"header":"dark","layout":"agency"} 
    return render(request,'pages/team/team-grid/team-grid.html',context)

def team_list(request):
    context={"header_logo":default_header_image,"header":"dark","layout":"agency"} 
    return render(request,'pages/team/team-list/team-list.html',context)

    # coming soon pages views

def coming_soon_1(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":default_header}
    return render(request,'pages/coming-soon/coming-soon/coming-soon.html',context)

def coming_soon_2(request):
    context = {"header_logo":default_header_image,"layout":default_layout,"header":default_header}
    return render(request,'pages/coming-soon/coming-soon2/coming-soon2.html',context)

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

    # header options views

def features_light_header(request):
    context = {"header_logo":default_header_image,"header":"dark","layout":""}
    return render(request,'features/header-option/header-light/header-light.html',context)

def features_dark_header(request):
    context = {"header_logo":header_logos["white_logo"],"header":"header-absolute","layout":""}
    return render(request,'features/header-option/header-dark/header-dark.html',context)

def features_glass_header(request):
    context = {"header_logo":default_header_image,"header":"dark","layout":""}
    return render(request,'features/header-option/header-transparent/header-transparent.html',context)

def features_logo_center(request):
    context = {"header_logo":default_header_image,"header":"yoga nav-abs header-rel","layout":""} 
    return render(request,'features/header-option/header-center-logo/header-center-logo.html',context)

def features_header_right_navigation(request):
    context = {"header_logo":default_header_image,"header":"app1 nav-abs ","layout":""}
    return render(request,'features/header-option/header-right-navigation/header-right-navigation.html',context)

    # breadcrumb option views

def features_classic_types(request):
    context = {"header_logo":default_header_image,"header":"dark","layout":"agency"}
    return render(request,'features/breadcrumb-option/breadcrumb/breadcrumb.html',context)

def features_breadcrumb_left(request):
    context = {"header_logo":default_header_image,"header":"dark","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-left/breadcrumb-left.html',context)

def features_breadcrumb_right(request):
    context = {"header_logo":default_header_image,"header":"dark","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-right/breadcrumb-right.html',context)

def features_breadcrumb_center(request):
    context = {"header_logo":default_header_image,"header":"dark","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-center/breadcrumb-center.html',context)

def features_breadcrumb_dark(request):
    context = {"header_logo":header_logos["white_logo"],"header":"header-absolute","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-dark/breadcrumb-dark.html',context)

def features_parallex_background(request):
    context = {"header_logo":header_logos["white_logo"],"header":"header-absolute","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-parallex-background/breadcrumb-parallex-background.html',context)

def features_with_background(request):
    context = {"header_logo":header_logos["white_logo"],"header":"header-absolute","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-background/breadcrumb-background.html',context)

def features_gallery_background(request):
    context = {"header_logo":header_logos["white_logo"],"header":"header-absolute","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-gallery-background/breadcrumb-gallery-background.html',context)

def features_video_background(request):
    context = {"header_logo":header_logos["white_logo"],"header":"header-absolute","layout":""}
    return render(request,'features/breadcrumb-option/breadcrumb-video-background/breadcrumb-video-background.html',context)

    # footer options views

def features_footer_default(request):
    context = {"header_logo":default_header_image,"header":"dark","layout":"","parent":"Footer Default","child":"Footer Style"}
    return render(request,'features/footer-options/footer-default/footer-default.html',context)
