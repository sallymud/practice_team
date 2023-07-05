from .models import TestMake, Question, Answer
from django.forms import ModelForm, TextInput

class TestForm(ModelForm):
    class Meta:
        model = TestMake
        fields = ['test_title']

        widgets = {
            "test_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название теста'
            })
        }