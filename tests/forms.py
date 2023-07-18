from .models import Test, Question, Answer
from django.forms import ModelForm, TextInput

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['name']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название теста'
            })
        }

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['test', 'questiontype', 'name', 'explanation']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['question', 'name', 'is_correct']