from django import forms
from .models import Listing, ListingImage, Review

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['rent', 'number_of_rooms', 'location', 'block', 'description']

class ImageForm(forms.ModelForm):
    class Meta:
        model = ListingImage
        fields = ['image']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review here...'}),
        }