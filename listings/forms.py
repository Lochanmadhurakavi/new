from django.forms import ModelForm
from .models import Listings



class ListingForm(ModelForm):
    class Meta:
        model = Listings
        fields = ['title', 
                  'price', 
                  'num_bedrooms', 
                  'num_bathrooms', 
                  'square_footage', 
                  'address',
                  'image']



