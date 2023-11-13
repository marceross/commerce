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
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    starting_bid = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField("date published")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} : {self.title} from: {self.category_id} starting bid: {self.starting_bid} created: {self.created_date}"

class Bid(models.Model):
    bid_user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid_time = models.DateTimeField("date bid")
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.bid

class Comment(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    comment_time = models.DateField("date comment")
    comment_text = models.CharField(max_length=500)

    def __str__(self):
        return self.comment

class Watchlist(models.Model):
    watch_user = models.ForeignKey(User, on_delete=models.CASCADE)
    watch_listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return self.watch_user


