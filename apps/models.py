from django.db.models import Model, CharField, ImageField, ForeignKey, CASCADE, TextField, IntegerField, FloatField


# TODO TASK 1

class Product(Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='product/image/')
    price = FloatField()
    discount_price = FloatField(null=True, blank=True)


    def __str__(self):
        return self.name

    @property
    def new_price(self):
        return self.price * (100 - self.discount_price) // 100

# class Account(Model):
#     name = CharField(max_length=255)
#     job = CharField(max_length=255)
#     image = ImageField(upload_to='user/image')
#
#     def __str__(self):
#         return self.name
#
#
# class Friend(Model):
#     name = CharField(max_length=255)
#     job = CharField(max_length=255)
#     image = ImageField(upload_to='friend/image')
#     user = ForeignKey('apps.Account', CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Category(Model):
#     name = CharField(max_length=255)
#     image = ImageField(upload_to='category/image')
#
# class Product(Model):
#     name = CharField(max_length=255)
#     description = TextField()
#     price = IntegerField(default=0)
#     category = ForeignKey('apps.Category', CASCADE)
#
#     def __str__(self):
#         return self.name
