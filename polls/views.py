"""View config for polls site."""

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from .models import Choice, Question


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
    user = request.user
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
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_passwd)
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))
        # what if form is not valid?
        # we should display a message in signup.html
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
