from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset = Author.objects.all(), label = "Auteur")

    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity']
        labels = {'title' : 'Titre', 'quantity' : 'Quantité'}

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']

        if quantity <= 0 or quantity > 100:
            raise forms.ValidationError("La quantité du livre doit être comprise entre 1 et 100")
        
        return quantity














































# class SomeForm(forms.Form):
#     username = forms.CharField(label = "Nom d'utilisateur", max_length = 25, required = False)
#     password = forms.CharField(label = "Mot de passe", widget = forms.PasswordInput, required = False)

#     bio = forms.CharField(label = "Biographie", widget = forms.Textarea, required = False)

#     languages = [('C', 'Langage C'), ('P', 'PHP')]
#     language = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple, required = False, label = "Langages connus", choices = languages) 

#     colors = [('1', 'Rouge'), ('2', 'Bleu'), ('3', 'Vert')]
#     color = forms.ChoiceField(choices = colors, label = "Radio de couleurs", required = False, widget = forms.RadioSelect)

#     countries = [('fr', 'France'), ('jp', 'Japon'), ('ru', 'Russie')]
#     country = forms.ChoiceField(choices = countries, label = "Pays")

#     publicate = forms.CharField(label = "Publier le contenu ? ", required = True, widget = forms.CheckboxInput)