import datetime

from django.db import models
from django.utils import timezone

def now_plus_30():
        return timezone.now() + datetime.timedelta(days=30)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=now_plus_30)
    
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def is_published(self):
        now = timezone.now()
        return now >= self.pub_date
    is_published.admin_order_field = 'pub_date'
    is_published.boolean = True
    is_published.short_description = 'Already published?'

    def can_vote(self):
        now = timezone.now()
        return self.end_date >= now >= self.pub_date 
    can_vote.boolean = True
    can_vote.short_description = 'Can vote?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text