import uuid
from django.db import models

class Question(models.Model):
    """
    Model representing Quizz Questions.
    """
    text = models.CharField(max_length=200)
    answer = models.ForeignKey('Answer', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Question " + str(self.id)

class Answer(models.Model):
    """
    Model representing Quizz Answers.
    """
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    C = models.CharField(max_length=100)
    D = models.CharField(max_length=100)
    Correct_Answer = models.CharField(max_length=1, help_text="Write the letter of the correct answer.", null=True)

    def __str__(self):
        return "Answer for Question " + str(self.id)

class Room(models.Model):
    """
    A unique room, having a 4 character UUID.
    """
    id = models.CharField(primary_key=True, max_length=4, blank=True, unique=True, default=uuid.uuid4)
