from django.contrib import admin
from .models import TestMake, Question, Answer, Results

admin.site.register(TestMake)

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Results)
