from django.views.generic import ListView, TemplateView


class ProductTemplateView(TemplateView):
    template_name = 'apps/product/product-grid.html'
