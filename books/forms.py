from django import forms
from .models import Publisher, Author, Book
from django.forms import ModelForm

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(ModelForm):
    publication_date = forms.DateField(
        label="Fecha de publicacion",
        input_formats=['%d/%m/%Y', '%Y-%m-%d'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder': 'DD/MM/AAAA'},
        )
    )
    
    class Meta:
        model = Book
        fields = '__all__'