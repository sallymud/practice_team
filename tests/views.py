from django.shortcuts import render, redirect
#from models import Question, Answer почему-то не хочет их подгружать

def tests_home(request):
    return render(request, 'tests/tests_home.html')

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
