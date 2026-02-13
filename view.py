from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission
from django.contrib.auth.decorators import login_required


@login_required
def submit_exam(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    selected_ids = request.POST.getlist('choice')

    submission = Submission.objects.create(
        user=request.user,
        course=course
    )

    submission.selected_choices.set(selected_ids)

    return redirect('show_exam_result', submission.id)


@login_required
def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    course = submission.course

    selected_choices = submission.selected_choices.all()
    selected_ids = [choice.id for choice in selected_choices]

    questions = Question.objects.filter(course=course)

    total_score = 0
    possible_score = 0

    for question in questions:
        possible_score += question.grade
        total_score += question.is_get_score(selected_ids)

    context = {
        'course': course,
        'selected_ids': selected_ids,
        'grade': total_score,
        'possible': possible_score
    }

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)

