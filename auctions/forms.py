from django import forms
from django.forms import inlineformset_factory
import datetime


from .models import Auction, Category, Comment, Bid

# Create list of categories

categories = Category.objects.all().values_list('name','name')
#print("Categories:", categories)

category_list = []

for category in categories:
    category_list.append(category)


class DateInput(forms.DateInput):
    input_type = 'date'

class AuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['title', 'description','category','image_url', 'price','end_date']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-2 specific-textarea'}),
            'category': forms.Select(choices=category_list,attrs={'class': 'form-control mb-2'}),
            'image_url': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'price': forms.TextInput(attrs={'class':'form-control mb-2'}),
            'end_date': DateInput(attrs={'class':'form-control mb-2',}),
        }
    
    def clean_end_date(self): #Validates the end_date
        end_date = self.cleaned_data.get('end_date')
        
        if end_date < datetime.date.today():
            raise forms.ValidationError('The date you entered has passed')
        return end_date
    

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['price']

        labels = {
           'price' : '',
        }

        widgets = {
            'price': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'placeholder': 'Place a bid.'}), 
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        labels = {
           'body' : '',
        }

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control comment-textarea', 'type':'text', 'placeholder': 'Add a comment.'}),
        }
    
