from django import forms

from .models import Todo

class ToDoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ('title', 'description')