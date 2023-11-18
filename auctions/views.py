from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Bid, Comment

from django import forms


class NewListing(forms.Form):
    title = forms.CharField (widget=forms.TextInput (attrs={'placeholder':'Enter title'}))
    description = forms.CharField (widget=forms.Textarea (attrs={'placeholder':'Enter a description of your products'}))
    starting_bid = forms.DecimalField
    created_date = forms.DateTimeField
    '''category_id = forms.Select'''

class NewBid(forms.Form):
    amount = forms.IntegerField

class AddWatch(forms.Form):
    search = forms.CharField(label="Search",required= False, widget= forms.TextInput (attrs={'placeholder':'Search Encyclopedia'}))
    '''un solo campo, sera como una casilla de verificacion??'''


# show a list of all the currently active auction listing
def index(request):
    return render(request, "auctions/index.html",
    {
        "listings": Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")


# a list of categories takes to a list of products inside a category with the active listings
def category(request):
    return render(request, "auctions/categories.html",
                  {
        "category": Category.objects.all()
    })
'''get_list_or_404()'''


# watchlist page of all the product added previoulsly to watchlist 
def watchlist(request):
    return render(request, "auctions/watchlist.html")


def create_page(request):
    if request.method== "POST":
        form = NewListing(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            form.listing.add(title, description)
            # por que no puedo agregar a la base?
            return Listing(request, title)
        else:
            return render(request, "auctions/create_listing.html", {"form": form
            })
        '''con el datalle de error o mensaje'''
    else:
        return render(request, "auctions/create_listing.html", {"form": NewListing()
        })

'''def listing(request):
    return render(request, "auctions/listings.html")'''


# take the user to a specific listing and see all details including the last bid or current price
# if user is signed in
# be able to add to watchlist, if the item is already in watchlist be able to remove it
# be able to place a bid on the item, at least as large as the starting bid and greater than the last bid if any. An error should display if the criteria is not met
# be able to close a bid if he is the one who created the item and the highest bidder turns into winner and makes the listing no longer active.

# close listing page??? same as this one, or similar... there should be a page saying that an auction was won by the signed in user
# be able to add comments to the listing page. All comments made should be displayed on that listing

def listing_page(request, listing_id):
    if request.method == "POST":
        try:
            listing = Listing.objects.get(pk=listing_id)
        except Listing.DoesNotExist:
            raise Http404("Listing not found.")
        return render(request, "auctions/listings.html",{
            "Title":listing,
        })
# error, context must be a dict rather than a set
# error, AttributeError at /1 'QuerySet' object has no attribute 'id'


def bid(request, listing_id):
    if request.method == "POST":
        try:
            bid = User.objects.get(pk=int(request.POST["user"]))
            listing = Listing.objects.get(pk=listing_id)
        except KeyError:
            return HttpResponseBadRequest("Bad Request: no bid")
        except Listing.DoesNotExist:
            return HttpResponseBadRequest("Bad Request: flight does not exist")
        bid.bid_amount.add(listing)
        return HttpResponseRedirect(reverse("listing", args=(listing_id,)))