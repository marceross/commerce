from django.urls import path

from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.category, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("create_page", views.create_page, name="create"),
    path("<int:listing_id>", views.listing_page, name="listing")
    # error NoReverseMatch at / solved when changing "listings" to "<int:listing_id>"
]
