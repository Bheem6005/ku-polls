"""View config for polls site."""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from polls.forms import CreateUserForm
from .models import Choice, Question, Vote


class IndexView(generic.ListView):
    """View config for polls index site."""

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the published questions (not including those set to be\
        published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')


class DetailView(generic.DetailView):
    """View config for polls detail site."""

    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """View config for polls result site."""

    model = Question
    template_name = 'polls/results.html'


@login_required(login_url='/accounts/login/')
def vote(request, question_id):
    """Voting method."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        already_vote = Vote.objects.filter(question=question_id, user=request.user).exists()
        if already_vote:
            get_vote = Vote.objects.get(user=request.user)
            get_vote.choice_id = selected_choice.id
            get_vote.save()
        else:
            get_vote = Vote.objects.create(question=question, user=request.user, choice=selected_choice)
            get_vote.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def signup(request):
    """Register a new user."""
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_passwd)
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))
    return render(request, 'registration/signup.html', {'form': form})


def index(request):
    """Redirect to the polls index."""
    return HttpResponseRedirect(reverse('polls:index'))
