from django import forms
from main.models import Comment, Contact, Email

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name', 'comment', 'image')
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your message'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'image': forms.ClearableFileInput(attrs={'required': False}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your message'})
        }

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        widgets = {
            'mail': forms.TextInput(attrs={'class': 'form control', 'placeholder': 'Enter email address'})
        }
