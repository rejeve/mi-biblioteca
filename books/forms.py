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
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
    )

    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        label="Autores",
        widget=forms.SelectMultiple(attrs={'class': 'tomselect'}))
    
    class Meta:
        model = Book
        fields = '__all__'