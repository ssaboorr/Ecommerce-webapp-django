from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


# Create your models here.

STATE_LIST = (
    ('Maharashtra','Maharashtra'),
    ('Delhi','Delhi'),
    ('Banglore','Banglore')
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_LIST,max_length=100)
    zip_address = models.IntegerField

    def __str__(self):
        return str(self.id)

CATEGORY_LIST = (
    ('Electronics','Electronics'),
    ('Clothing','Clothing'),
    ('Footwear','Footwear')
)

SUB_CATEGORY_LIST = (
    ('Mobiles','Mobiles'),
    ('Tablets','Tablets'),
    ('Laptops & PC','Laptops & PC'),
    ('Gaming','Gaming'),
    ('Top-wear','Top-wear'),
    ('Bottom-wear','Bottom-wear'),
    ('Jackets','Jackets'),
    ('Casual','Casual'),
    ('Sports','Sports'),
)

class  Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_LIST,max_length=100)
    sub_category = models.CharField(choices=SUB_CATEGORY_LIST,max_length=200)
    brand = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return str(self.id)

class  Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)



STATUS_LIST = (
    ('Pending','Pending'),
    ('Order Received','Order Received'),
    ('Packed','Packed'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')


)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(choices=STATUS_LIST,max_length=100,default='Pending')



