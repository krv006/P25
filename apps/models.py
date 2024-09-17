from django.db.models import Model, CharField, ImageField, ForeignKey, CASCADE, TextField, IntegerField


# TODO TASK 1

class Account(Model):
    name = CharField(max_length=255)
    job = CharField(max_length=255)
    image = ImageField(upload_to='user/image')

    def __str__(self):
        return self.name


class Friend(Model):
    name = CharField(max_length=255)
    job = CharField(max_length=255)
    image = ImageField(upload_to='friend/image')
    user = ForeignKey('apps.Account', CASCADE)

    def __str__(self):
        return self.name


class Category(Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='category/image')

class Product(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = IntegerField(default=0)
    category = ForeignKey('apps.Category', CASCADE)

    def __str__(self):
        return self.name
