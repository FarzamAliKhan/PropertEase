
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField, ModelForm
from .models import *
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django import forms


class ListingForm(ModelForm):

    class Meta:
        model = Listing


        widgets={
            'mobile_num': PhoneNumberPrefixWidget(initial='PK', attrs={'style': 'max-width: 250px;'}),            
    
        }
        fields = [
            "title",
            "purpose",
            "property_type",
            "price",
            "num_bedrooms",
            "num_bathrooms",
            "area_size",
            "city",
            "location",
            "plot_number",
            "description",
            "email",
            "mobile_num",
            "map_link",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
        ]



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2',
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'body']