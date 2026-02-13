from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission
from django.contrib.auth.decorators import login_required


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course)
    questions = Question.objects.filter(course=course)

    return render(request, 'onlinecourse/course_details_bootstrap.html', {
        'course': course,
        'lessons': lessons,
        'questions': questions
    })


@login_required
def submit_exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    selected_ids = request.POST.getlist('choice')
    choices = Choice.objects.filter(id__in=selected_ids)

    submission = Submission.objects.create(
        user=request.user,
        course=course
    )

    submission.selected_choices.set(choices)

    return redirect('show_exam_result', submission.id)


@login_required
def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    score = submission.calculate_score()

    return render(request, 'onlinecourse/exam_result.html', {
        'submission': submission,
        'score': score
    })
