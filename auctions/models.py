from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} {self.description}" 

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User)
    image_url = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.title} {self.starting_bid} {self.created_date} {self.category_id}"

class Bid(models.Model):
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid_time = models.DateTimeField(auto_now_add=True)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.bid_user} {self.bid_listing} {self.bid_time} {self.bid_amount}"

class Comment(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_text = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.comment_user} {self.comment_listing} {self.comment_time} {self.comment_text}"

# class Watchlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     listing = models.ManyToManyField(Listing)

#     def __str__(self):
#         return f"{self.user}"