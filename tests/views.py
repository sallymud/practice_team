from django.shortcuts import render, redirect, get_object_or_404
from .models import TestMake, Question, Answer
from .forms import TestForm
from django.contrib import messages

def tests_home(request):
    return render(request, 'tests/tests_home.html')

def create(request):
    if request.method == 'POST':
        test_title = request.POST.get('test_title')
        if TestMake.objects.filter(test_title=test_title).exists():
            # Значение уже существует, выдать ошибку
            messages.error(request, 'Тест с таким названием уже существует!')
            return redirect('create')
        else:
            # Значение уникальное, сохранить в базу данных
            test = TestMake(test_title=test_title)  # создаем экземпляр модели
            test.save()  # сохраняем в базу данных
            messages.success(request, 'Тест успешно создан.')
            return redirect('create')
    form = TestForm()
    return render(request, 'tests/create.html', {'form': form})

def test_list(request):
    tests = TestMake.objects.all()
    return render(request, 'tests/test_list.html', {'tests': tests})

def test_detail(request, test_id):
    test = get_object_or_404(TestMake, id=test_id)
    questions = Question.objects.filter(testmakers=test)

    if request.method == 'POST':
        for question in questions:
            answer_id = request.POST.get('questiom_{}'.format(question.id))
            answer = get_object_or_404(Answer, id=answer_id)
            # Обработка ответа пользователя
    data = {
        'tests': test,
        'questions': questions
    }
    return render(request, 'tests/test_detail.html', data)



''' ФУНКЦИЯ ДЛЯ ПОДСЧЁТА ОЧКОВ ЗА ПРАВИЛЬНЫЕ ОТВЕТЫ С ПЕРЕХОДОМ НА СТРАНИЦУ СО СЧЁТОМ И ОБРАТНО НА ВОПРОС
def test_view_result(request):
    if request.method == "POST":
        score=0
        your_answer=request.POST.getlist(answer)
        for answer_id in your_answer:
            answer=Answer.objects.get(is=answer_id)
            if answer.is_correct:
                score+=1
        return render(request,'score',{'':score}) # в скобках указать html файл для страницы с кол-вом баллов
    question=Question.objects.all()
    return render(request,'question',{'':question}) # в скобках указать html файл для страницы с вопросом
'''
