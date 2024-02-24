from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('create-order/', views.create_order, name='create_order'),
    # path('order_change/', views.order_change, name='order_change'),
    # path('order_remove/', views.order_remove, name='order_remove'),
]