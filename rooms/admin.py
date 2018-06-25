from django.contrib import admin
from .models import Answer, Question, Room

# admin.site.register(Question)
admin.site.register(Room) #rm


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'A', 'B', 'C', 'D', 'Correct_Answer')
    fields = [('A', 'B', 'C', 'D'), 'Correct_Answer']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
