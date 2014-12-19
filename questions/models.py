from django.db import models
from django.contrib.auth.models import User
from discussions.models import Thread


class Solution(models.Model):
    solution_text = models.TextField()

    def __str__(self):
        return self.solution_text[:50]


class Source(models.Model):
    source_name = models.CharField(max_length=64)
    source_url = models.CharField(max_length=256)

    def __str__(self):
        return self.source_name


class Question(models.Model):
    MATH = "MATH"
    PMATH = "PMATH"
    CS = "CS"
    CO = "CO"
    STAT = "STAT"
    ACTSCI = "ACTSCI"
    AMATH = "AMATH"

    SUBJECTS = (
        (MATH, "Mathematics"),
        (PMATH, "Pure Mathematics"),
        (CS, "Computer Science"),
        (CO, "Combinatorics and Optimization"),
        (STAT, "Statistics"),
        (ACTSCI, "Actuarial Science"),
        (AMATH, "Applied Mathematics"),
    )

    E = "E"
    M = "M"
    H = "H"

    DIFFICULTY = (
        (E, "Easy"),
        (M, "Medium"),
        (H, "Hard"),
    )

    question_title = models.CharField(max_length=64)
    question_text = models.TextField()

    subject = models.CharField(max_length=5, choices=SUBJECTS, default=MATH)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY, default=M)

    solution = models.ForeignKey(Solution, blank=True, null=True)
    # lesson = models.ForeignKey(Lesson, blank=True, null=True)
    source = models.ForeignKey(Source, blank=True, null=True)
    # discussion = models.ForeignKey(Thread, editable=False)

    def __str__(self):
        return "{0} - {1}: {2}".format(self.difficulty, self.subject,
                                       self.question_title[:50])

    def save(self):
        if not self.id:
            self.discussion = Thread.objects.create_thread(User.objects.get(id=1), self.question_title, self.subject)
        super(Question, self).save()