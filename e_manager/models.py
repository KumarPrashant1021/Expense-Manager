from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    monthlyIncome = models.DecimalField(default = 0,max_digits=15,decimal_places=0,null=True)
    def __str__(self):
        return self.user.username
    
class ExpenseDetails(models.Model):
    category_choice = (
        ('Food','Food'),
        ('Social Life','Social life'),
        ('Education','Education'),
        ('Household','Household'),
        ('Transportation','Transportation'),
        ('Fashion','Fashion'),
        ('Health','Health'),
        ('Self Development','Self development'),
        ('Gift','Gift'),
        ('Other','Other'),
        )

    accounts_choice = (
        ('Cash','Cash'),
        ('Card','Card')
        )
    
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
    date = models.DateField()
    category = models.CharField(max_length=50,choices=category_choice)
    accounts = models.CharField(max_length=50,choices=accounts_choice)
    contents =  models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
       return self.customer.user.username

    

    

        
