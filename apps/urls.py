from django.urls import path

from apps.views import profil_page, product_page, index

urlpatterns = [
    path('profil/', profil_page, name='profil_page'),
    path('product/page/<int:pk>', product_page, name='product_page'),
    path('category/', index, name='index-page')
]
