from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import TestForm

def tests_home(request):
    return render(request, 'tests/tests_home.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TestForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'tests/create.html', data)



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
