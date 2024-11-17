from django.urls import path
from .views import create_product_ajax, create_product_flutter, delete_product, login_user, logout_user, show_product, register_user, show_json, show_json_by_id, show_main, create_product, show_xml, show_xml_by_id, update_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),

    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('product-ajax', create_product_ajax, name='create_product_ajax'),
    path('product-flutter/', create_product_flutter, name='create_mood_flutter'),

    path('product/', create_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('product/<str:id>/edit', update_product, name='update_product'),
    path('product/<str:id>/delete', delete_product, name='delete_product'),

    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<str:id>/', show_json_by_id, name='show_json'),
]
