from django.db import models

class TestMake(models.Model):
    test_title = models.CharField('Название теста', max_length=100)

    def __str__(self):
        return self.test_title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    testmakers = models.ForeignKey(TestMake, on_delete=models.CASCADE)
    question_text = models.CharField('Текст вопроса', max_length=200)
    marks = models.IntegerField('Баллы', default=5)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField('Верный ответ', default=False)

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'