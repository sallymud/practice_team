from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from users.utils import paginateObjects
from .models import Test, Question, Answer, Results, Choice
from .forms import TestForm, QuestionForm, AnswerForm
from django.contrib import messages


@login_required
def tests(request):
    tests = Test.objects.all()
    custom_range, tests = paginateObjects(request,
        tests, 3)
    context = {'tests':tests, 'custom_range': custom_range}
    return render(request, 'tests/test_list.html', context)

@login_required
def display_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    question = test.question_set.first()
    return redirect(reverse('display_question',
        kwargs={'test_id': test_id,
        'question_id': question.pk}))

@login_required
def display_question(request, test_id, question_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = test.question_set.all()
    current_question, next_question = None, None
    for ind, question in enumerate(questions):
        if question.pk == question_id:
            current_question = question
            if ind != len(questions) - 1:
                next_question = questions[ind + 1]
    context = {'test': test,
    'question': current_question,
    'next_question': next_question}
    return render(request,
        'tests/test_detail.html',context)

@login_required
def grade_question(request, test_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    test = get_object_or_404(Test, pk=test_id)
    can_answer = question.user_can_answer(request.user)
    try:
        if not can_answer:
            return render(request,
                'tests/gap.html',
                {'question': question,
                'error_message': 'Вы уже отвечали на этот вопрос.'})

        if question.questiontype == 'single':
            correct_answer = question.get_answers()
            user_answer = question.answer_set.get(pk=request.POST['answer'])
            choice = Choice(user=request.user,
                question=question, answer=user_answer)
            choice.save()
            is_correct = correct_answer == user_answer
            result, created = Results.objects.get_or_create(user=request.user,
                test=test)
            if is_correct is True:
                result.correct = F('correct') + 1
            else:
                result.wrong = F('wrong') + 1
            result.save()

        elif question.questiontype == 'multiple':
            correct_answer = question.get_answers()
            answers_ids = request.POST.getlist('answer')
            user_answers = []
            if answers_ids:
                for answer_id in answers_ids:
                    user_answer = Answer.objects.get(pk=answer_id)
                    user_answers.append(user_answer.name)
                    choice = Choice(user=request.user,
                        question=question, answer=user_answer)
                    choice.save()
                is_correct = correct_answer == user_answers
                result, created = Results.objects.get_or_create(user=request.user,
                    test=test)
                if is_correct is True:
                    result.correct = F('correct') + 1
                else:
                    result.wrong = F('wrong') + 1
                result.save()

    except:
        return render(request, 'tests/gap.html', {'question': question})
    return render(
            request, 'tests/gap.html',
            {'is_correct': is_correct,
            'correct_answer': correct_answer,
            'question': question})

@login_required
def test_results(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    questions = test.question_set.all()
    results = Results.objects.filter(user=request.user,
        test=test).values()
    correct = [i['correct'] for i in results][0]
    wrong = [i['wrong'] for i in results][0]
    context = {'test': test,
    'correct': correct,
    'wrong': wrong,
    'number': len(questions),
    'skipped': len(questions) - (correct + wrong)}
    return render(request, 'tests/results.html', context)


def tests_home(request):
    return render(request, 'tests/tests_home.html')


def create(request):
    if request.method == 'POST':
        test_form = TestForm(request.POST)
        if test_form.is_valid():
            name = test_form.cleaned_data['name']
            if Test.objects.filter(name=name).exists():
                # Значение уже существует, выдать ошибку
                messages.error(request, 'Тест с таким названием уже существует!')
                return redirect('create')

            test = test_form.save()

            questions = request.POST.getlist('name')
            explanations = request.POST.getlist('explanation')
            questiontypes = request.POST.getlist('questiontype')
            answers = request.POST.getlist('answer_text[]')
            is_correct = request.POST.getlist('is_correct[]')

            for i in range(len(questions)):
                question = Question(test=test, questiontype=questiontypes[i], name=questions[i], explanation=explanations[i])
                question.save()

                for j in range(i*2, (i*2)+2):
                    answer = Answer(question=question, answer_text=answers[j], is_correct=bool(int(is_correct[j])))
                    answer.save()

            messages.success(request, 'Тест успешно создан.')
            return redirect('create')
    else:
        test_form = TestForm()

    return render(request, 'tests/create.html', {'test_form': test_form})


"""
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

    return render(request, 'tests/test_results.html', data)"""




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