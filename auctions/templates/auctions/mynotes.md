Would be nice trying to add a utils.py file for the listing view

For the site
Marce
marceross@gmail.com
1234

Cris
1234


For superuser....................
Username: Juan
Email address: juan@gmail.com
Password:  1234
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.


Django commands
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

python manage.py cratesuperuser


Again had to delete last migration... UNDONE
Insted I could

Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> timezone.now
Migrations for 'auctions':
  auctions\migrations\0007_listing_closed_listing_created_by.py
    - Add field closed to listing
    - Add field created_by to listing
PS C:\Users\Usuario\commerce> 

TIME WAS NOT GOOD
I JUST PUT ANOTHER 1 AND WORKED FINE...



WARNINGS:
auctions.Bid: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
        HINT: Configure the DEFAULT_AUTO_FIELD setting or the AuctionsConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
auctions.Category: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.

settings.py line 86
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'



SELECTED OPTION 1 BELOW
It is impossible to add a non-nullable field 'created_by' to listing without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 2



Had to delete last migration inside migrations folder
Delete db.sqlite3
So I could makemigrations again, keep getting errors when trying to add field for the image_url

Understanding ManyToManyField
https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django




class Listing(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
hice este cambio porque creo que habia que poner la fecha manualmente, por lo menos parece funcionar bien

class NewListing(forms.ModelForm):
        class Meta:
            model = Listing
            exclude = ["created_date", "followers"]



Wishlist

Copiar de github a visualstudio

https://www.geeksforgeeks.org/meta-class-in-models-django/
class meta, exclude[ ]

https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/
create forms from models, conventions

Lista categories
Actualice urls.py
cree category.html
en views agregue la parte de categories



