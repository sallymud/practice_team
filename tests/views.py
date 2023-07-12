from django.shortcuts import render, redirect, get_object_or_404
from .models import TestMake, Question, Answer, Results
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
        score = 0
        total_marks = 0

        for question in questions:
            answer_id = request.POST.get('questiom_{}'.format(question.id))
            answer = get_object_or_404(Answer, id=answer_id)

            if answers.filter(is_correct=True).exists():
                score += question.mark
            total_marks += question.mark

            percentage_score = (score / total_marks) * 100
            result = Results(user=request.user, test=test, score=percentage_score)
            result.save()

            return redirect('test_results', test_id=test.id)

    data = {
        'test_id': test_id,
        'tests': test,
        'questions': questions
    }
    return render(request, 'tests/test_detail.html', data)


def test_results(request, test_id):
    test = get_object_or_404(TestMake, id=test_id)
    user_result = Results.objects.filter(user=request.user, test=test).first()

    total_marks = 0
    score = 0
    percentage_score = 0

    if user_result:
        questions = Question.objects.filter(testmakers=test, marks=marks)
        total_marks = sum(question.marks for question in questions)

        for question in questions:
            # correct_answers = Answer.objects.filter(question=question, is_correct=True)
            user_answers = user_result.get_user_answers(question.id)

            if user_answers.is_correct == True:
                score += question.marks

        percentage_score = (score / total_marks) * 100

    data = {
        'test': test,
        'score': score,
        'percentage_score': percentage_score,
        'total_marks': total_marks,
    }

    return render(request, 'tests/test_results.html', data)




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