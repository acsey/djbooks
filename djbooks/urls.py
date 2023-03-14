from django.urls import path
from . import views

app_name = 'djbooks'

urlpatterns = [
    
    # home paths

    path('',views.index,name='index'),
 
    # pages paths

    path('pages_404',views.pages_404,name='pages_404'),
    path('faqs',views.faqs,name='faqs'),
    path('collection',views.collection,name='collection'),
    path('typography',views.typography,name='typography'),
    path('maintenance',views.maintenance,name='maintenance'),
    path('about_us',views.about_us,name='about_us'),

        # team paths

    path('team',views.team,name='team'),
    path('team_grid',views.team_grid,name='team_grid'),
    path('team_list',views.team_list,name='team_list'),

        # coming soon paths

    path('coming_soon_1',views.coming_soon_1,name='coming_soon_1'),
    path('coming_soon_2',views.coming_soon_2,name='coming_soon_2'),



    # shop categories paths

    path('shop_categories_left_sidebar',views.shop_categories_left_sidebar,name='shop_categories_left_sidebar'),
    path('shop_categories_two_sidebar',views.shop_categories_two_sidebar,name='shop_categories_two_sidebar'),
    path('shop_categories_three_sidebar',views.shop_categories_three_sidebar,name='shop_categories_three_sidebar'),
    path('shop_categories_six_sidebar',views.shop_categories_six_sidebar,name='shop_categories_six_sidebar'),
    path('shop_categories_right_sidebar',views.shop_categories_right_sidebar,name='shop_categories_right_sidebar'),
    path('shop_categories_right_2_grid',views.shop_categories_right_2_grid,name='shop_categories_right_2_grid'),
    path('shop_categories_right_3_grid',views.shop_categories_right_3_grid,name='shop_categories_right_3_grid'),
    path('shop_categories_right_6_grid',views.shop_categories_right_6_grid,name='shop_categories_right_6_grid'),
    path('shop_categories_no_sidebar',views.shop_categories_no_sidebar,name='shop_categories_no_sidebar'),
    path('shop_categories_no_sidebar_2',views.shop_categories_no_sidebar_2,name='shop_categories_no_sidebar_2'),
    path('shop_categories_no_sidebar_3',views.shop_categories_no_sidebar_3,name='shop_categories_no_sidebar_3'),
    path('shop_categories_no_sidebar_6',views.shop_categories_no_sidebar_6,name='shop_categories_no_sidebar_6'),
    path('shop_categories_metro',views.shop_categories_metro,name='shop_categories_metro'),

    # product page paths

    path('shop_product_no_sidebar',views.shop_product_no_sidebar,name='shop_product_no_sidebar'),
    path('shop_product_left_sidebar',views.shop_product_left_sidebar,name='shop_product_left_sidebar'),
    path('shop_product_right_sidebar',views.shop_product_right_sidebar,name='shop_product_right_sidebar'),
    path('shop_product_3_grid',views.shop_product_3_grid,name='shop_product_3_grid'),
    path('books',views.books,name='books'),
    path('shop_product_3_grid_right',views.shop_product_3_grid_right,name='shop_product_3_grid_right'),
    path('shop_product_accordian',views.shop_product_accordian,name='shop_product_accordian'),
    path('shop_product_bundle',views.shop_product_bundle,name='shop_product_bundle'),
    path('shop_product_image_swatch',views.shop_product_image_swatch,name='shop_product_image_swatch'),
    path('shop_product_image_outside',views.shop_product_image_outside,name='shop_product_image_outside'),
    path('shop_product_image_sticky',views.shop_product_image_sticky,name='shop_product_image_sticky'),

    # shop pages paths

    path('shop_pages_cart',views.shop_pages_cart,name='shop_pages_cart'),
    path('shop_pages_checkout',views.shop_pages_checkout,name='shop_pages_checkout'),
    path('shop_pages_compare',views.shop_pages_compare,name='shop_pages_compare'),
    path('shop_pages_compare_2',views.shop_pages_compare_2,name='shop_pages_compare_2'),
    path('shop_pages_signup',views.shop_pages_signup,name='shop_pages_signup'),
    path('shop_pages_login',views.shop_pages_login,name='shop_pages_login'),
    path('shop_pages_wishlist',views.shop_pages_wishlist,name='shop_pages_wishlist'),

    # header options paths

    path('features_light_header',views.features_light_header,name='features_light_header'),
    path('features_dark_header',views.features_dark_header,name='features_dark_header'),
    path('features_glass_header',views.features_glass_header,name='features_glass_header'),
    path('features_logo_center',views.features_logo_center,name='features_logo_center'),
    path('features_header_right_navigation',views.features_header_right_navigation,name='features_header_right_navigation'),

    # bradcrumb paths

    path('features_classic_types',views.features_classic_types,name='features_classic_types'),
    path('features_breadcrumb_left',views.features_breadcrumb_left,name='features_breadcrumb_left'),
    path('features_breadcrumb_right',views.features_breadcrumb_right,name='features_breadcrumb_right'),
    path('features_breadcrumb_center',views.features_breadcrumb_center,name='features_breadcrumb_center'),
    path('features_breadcrumb_dark',views.features_breadcrumb_dark,name='features_breadcrumb_dark'),
    path('features_parallex_background',views.features_parallex_background,name='features_parallex_background'),
    path('features_with_background',views.features_with_background,name='features_with_background'),
    path('features_gallery_background',views.features_gallery_background,name='features_gallery_background'),
    path('features_video_background',views.features_video_background,name='features_video_background'),

    # footer options paths

    path('features_footer_default',views.features_footer_default,name='features_footer_default'),

    # custom types paths

    path('products',views.products,name='products'),
    #path("<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
    #path('books/<slug>', views.BookDetailView.as_view(), name='book_detail'),
    path('<slug:slug>', views.BookDetailView.as_view(), name='book_detail'),
    #path('books/<str:slug>', views.BookDetailView.as_view(), name='book_detail'),

]
