from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Account, Friend, Product, Category


# admin.site.register(Account)

@admin.register(Account)
class AccountAdmin(ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Friend)
class FriendAdmin(ModelAdmin):
    pass
