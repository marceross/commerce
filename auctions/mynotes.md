# models.py

Users
Category, need a model so not to repeat this info in every listing, also if I'd like to delete a whole category every listing can be erased as well
Listing
Bid, related to the listing and to the user, this way I can have an ID that relates to both of them, in case a user or a product is deleted all bids are erased with them
Comment, same as Bid



python manage.py makemigrations
python manage.py migrate

WARNINGS:
auctions.Bid: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the AuctionsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.



# admin.py

python manage.py createsuperuser
this is a different user than the one I've created from the /admin. I found the checkbox superuser status selected

(Terminal)
Username: marce
Error: That username is already taken.
Username: Marce
Email address: marceross@gmail.com
Password:
Password (again):
Error: Your passwords didn't match.
Password: 
Password (again):
Superuser created successfully.
PS C:\Users\Usuario\commerce> python manage.py runserver 



