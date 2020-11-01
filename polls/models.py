"""Model config for polls app."""

import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def now_plus_30():
    """Return DateTime of the next 30 days."""
    return timezone.now() + datetime.timedelta(days=30)


class Question(models.Model):
    """Question model."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=now_plus_30)

    def __str__(self):
        """Return the human-readable representation of an object."""
        return self.question_text

    def was_published_recently(self):
        """Check the question was published recently or not."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def is_published(self):
        """Check the question already published or not."""
        now = timezone.now()
        return now >= self.pub_date

    is_published.admin_order_field = 'pub_date'
    is_published.boolean = True
    is_published.short_description = 'Already published?'

    def can_vote(self):
        """Check the question can be voted or not."""
        now = timezone.now()
        return self.end_date >= now >= self.pub_date

    can_vote.boolean = True
    can_vote.short_description = 'Can vote?'


class Choice(models.Model):
    """Choice model."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        """Return the human-readable representation of an object."""
        return self.choice_text


class Vote(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
