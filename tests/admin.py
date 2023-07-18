from django.contrib import admin
from .models import Test, Question, Answer, Results, Choice


class AnswerAdmin(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Test)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Choice)
admin.site.register(Results)
