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
    path('request_book',views.request_book,name='request_book'),

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

    path('shop_pages_compare',views.shop_pages_compare,name='shop_pages_compare'),
    path('shop_pages_compare_2',views.shop_pages_compare_2,name='shop_pages_compare_2'),
    path('shop_pages_signup',views.shop_pages_signup,name='shop_pages_signup'),
    path('shop_pages_login',views.shop_pages_login,name='shop_pages_login'),
    path('shop_pages_wishlist',views.shop_pages_wishlist,name='shop_pages_wishlist'),

    # custom types paths

    #path("<slug:slug>", ArticleDetailView.as_view(), name="article_detail"),
    path('accounts/login/', views.BotLoginView.as_view(),name='login'),
    path('carrito', views.OrderSummaryView.as_view(), name='order-summary'),
    path('checkout', views.CheckoutView.as_view(), name='checkout'),
    path('buscar_libro', views.search_view, name='buscar_libro'), 
    path('<slug:slug>', views.BookDetailView.as_view(), name='book_detail'),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', views.remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    #p TODO: Rename this views
    path('libros-antiguos',views.shop_categories_no_sidebar_6,name='shop_categories_no_sidebar_6'),
    path('libros-firmados',views.shop_categories_no_sidebar_2,name='shop_categories_no_sidebar_2'),
    path('primeras-ediciones',views.shop_categories_no_sidebar_3,name='shop_categories_no_sidebar_3'),

]
