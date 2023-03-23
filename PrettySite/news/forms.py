from .models import Posts
from django.forms import ModelForm, TextInput, Textarea


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'anons', 'text']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form_input form-name-input',
                'placeholder': "name",
                'maxlength': "50",
                'required': True
            }),
            'anons': TextInput(attrs={
                'class': "form_input form-anons-input",
                'placeholder': "anons",
                'maxlength': "250",
                'required': True
            }),
            'text': Textarea(attrs={
                'class': "form_input form-text-input",
                'placeholder': "your post text",
                'required': True
            }),
        }
