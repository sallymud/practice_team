from .models import TestMake, Question, Answer
from django import forms
from django.forms import ModelForm, TextInput, Textarea, NumberInput

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

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'marks']

        widgets = {
            "question_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст вопроса'
            }),
            "marks": NumberInput(attrs={
                'class': 'form-control form-outline',
                'placeholder': 'Баллы',
            })
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'is_correct']

        widgets = {
            "answer_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Текст ответа'
            }),
            "is_correct": forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
