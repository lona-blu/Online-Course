from django.contrib import admin
from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission
)


# Inline for Choices inside Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Inline for Questions inside Course
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'course', 'grade')
    inlines = [ChoiceInline]


# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')


# Course Admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


# Register Models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
