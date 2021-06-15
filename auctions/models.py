from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass

class Auction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=220, null=True)
    image_url = models.URLField(max_length=600, default=None)
    category = models.CharField(max_length=120, default=None)
    price = models.DecimalField(decimal_places=2, max_digits=10000, default=None)
    date = models.DateTimeField(auto_now_add=True) 
    end_date = models.DateField()
    status = models.CharField(max_length=6, default="Open")
    highest_bid = models.DecimalField(decimal_places=2, max_digits=10000, null=True, default=0)
    highest_bidder = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
   
class Category(models.Model):
    name = models.CharField(max_length=120, default=None)

    def __str__(self):
        return self.name

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, default=None)

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, default=None)
    price = models.DecimalField(decimal_places=2, max_digits=100000, default=None)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    body = models.TextField(max_length=220, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.auction.title, self.user)