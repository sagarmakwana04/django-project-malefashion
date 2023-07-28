from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    address=models.TextField()
    password=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='profile_pic/',default='')
    usertype=models.CharField(max_length=100,default='buyer')

    def __str__(self):
        return self.fname+" "+self.lname
    
class Product(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    category=(
        ('Round','Round'),
        ('Polo','Polo'),
        ('Full Sleeve','Full Sleeve'),
        ('Sports','Sports'),
    )
    product_category=models.CharField(max_length=100,choices=category)
    brand=(
        ('Superdry','Superdry'),
        ('Allen Solly','Allen Solly'),
        ('Netplay','Netplay'),
        ('Performax','Performax'),
        ('Levis','Levis'),
    )
    product_brand=models.CharField(max_length=100,choices=brand)
    product_name=models.CharField(max_length=100)
    product_price=models.PositiveIntegerField()
    size=(
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
    )
    product_size=models.CharField(max_length=100,choices=size)
    product_pic=models.ImageField(upload_to='product_pic/')
    
    def __str__(self):
        return self.seller.fname+' - '+self.product_name

class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.fname+' - '+self.product.product_name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_price=models.PositiveIntegerField()
    product_qty=models.PositiveIntegerField(default=1)
    total_price=models.PositiveIntegerField()
    payment_status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.fname+' - '+self.product.product_name
