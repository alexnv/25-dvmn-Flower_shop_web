from django.urls import path

from .views import index_page, send_bunch, send_categories, send_reasons, \
    create_order, send_orders, send_random_bunch, remove_order, catalog_page, quiz_page, add_callback_lead, show_card, order_page, thankyou_page

# app_name = "webshop"

urlpatterns = [
    path('', index_page, name="index_page"),
    path('catalog/', catalog_page, name="catalog"),
    path('quiz/', quiz_page, name="quiz"),
    path('callback_add', add_callback_lead, name="lead_add"),
    path('card/<int:id>', show_card, name="card"),
    path('order/bunch-<str:bunch_id>/step-<str:step>/', order_page, name="order"),
    path('thankyou', thankyou_page, name="thankyou"),
    path('bunch/send/', send_bunch),
    path('categories/send/', send_categories),
    path('reasons/send/', send_reasons),
    path('order/create/', create_order),
    path('courier/send/', send_orders),
    path('random_bunch/send/', send_random_bunch),
    path('order/delete/', remove_order),
]
