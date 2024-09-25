from django.urls import path

from apps.views import ProductTemplateView

urlpatterns = [
    path('product', ProductTemplateView.as_view(), name='product-list-page')
]
