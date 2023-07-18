from django.db import models

from django.conf import settings

from users.models import CustomUser


class Test(models.Model):
    name = models.CharField('Название теста', max_length=100, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    class questiontype(models.TextChoices):
        single = 'single'
        multiple = 'multiple'

    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    questiontype = models.CharField(max_length=8, choices=questiontype.choices, default=questiontype.single)
    name = models.CharField('Текст вопроса', max_length=200)
    explanation = models.CharField('Правильный ответ', max_length=250, default='') #отображается после того как ответил


    def get_answers(self):
        if self.questiontype == 'single':
            return self.answer_set.filter(is_correct=True).first()
        else:
            qs = self.answer_set.filter(is_correct=True).values()
            return [i.get('name') for i in qs]


    def user_can_answer(self, user):
        user_choices = user.choice_set.all()
        done = user_choices.filter(question=self)
        print(done)
        if done.exists():
            return False
        return True

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField('Ответ', max_length=200, default='')
    is_correct = models.BooleanField('Верный ответ', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Choice(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Results(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    correct = models.IntegerField('Правильные ответы', default=0)
    wrong = models.IntegerField('Неправильные ответы', default=0)

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
