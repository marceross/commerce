from django.urls import path

from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("closed_listings", views.closed_listings, name="closed_listings"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:category_id>", views.category, name="category"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create_page", views.create_page, name="create"),
    path("<int:listing_id>", views.listing_page, name="listing")
    # error NoReverseMatch at / solved when changing "listings" to "<int:listing_id>"
]