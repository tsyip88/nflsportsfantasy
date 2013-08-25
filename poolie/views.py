from django.shortcuts import render, redirect
from django import forms
import django.contrib.auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import PasswordChangeForm
from matchups.utilities import week_number_for_last_matchup, matchups_for_week
import matchups.matchup_data_retriever
from matchups.models import Matchup, TieBreaker
import teams.team_data_retriever
import teams.models
import blog.models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

def login(request):
    redirect_to = request.GET.get('next', None)
    form = LoginForm()
    error_message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = django.contrib.auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    django.contrib.auth.login(request, user)
                    if redirect_to:
                        return redirect(redirect_to)
                    return render(request, 'successful_login.html')
                else:
                    error_message = "Unable to login due to disabled account."
            else:
                error_message = "Failed to log in. Please try again."
        else:
            error_message = "Failed to log in. Please try again."
    context = {'login_form':form,
               'error_message':error_message,
               'redirect_to':redirect_to}
    return render(request, 'login.html', context)

def logout(request):
    django.contrib.auth.logout(request)
    return render(request, 'successful_logout.html')

def index(request):
    all_blogs = blog.models.BlogPost.objects.all().order_by('-date_time')
    max_number_of_blog_posts_per_page = 5
    if all_blogs.count() > max_number_of_blog_posts_per_page:
        displayed_blogs = all_blogs[0:max_number_of_blog_posts_per_page]
    else:
        displayed_blogs = all_blogs
    context = {'blog_posts':displayed_blogs}
    return render(request, "index.html", context)

@login_required
def user_options(request):
    return render(request, "user_options.html")

@login_required
def change_password(request):
    error_message = ''
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            print "Change!"
        else:
            error_message = "Failed to change password. Please try again."
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form,
               'error_message':error_message}
    return render(request, "change_password.html", context)

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    verify_new_password = forms.CharField(max_length=50, widget=forms.PasswordInput)

@permission_required('matchups.add_matchup')
def admin_actions(request):
    if request.method == 'POST':
        if request.POST.has_key('load_matchups'):
            matchups.matchup_data_retriever.MatchupDataRetriever.load_matchups()
        if request.POST.has_key('load_teams'):
            sport_name = "football"
            league_name = "nfl"
            teams.team_data_retriever.TeamDataRetriever.load_teams(sport_name, league_name)
        if request.POST.has_key('load_images'):
            team_list = teams.models.Team.objects.all()
            for team in team_list:
                team.image_location = team.full_name().replace(' ','').replace('.','') + '.png'
                team.save()
    return render(request, "admin_actions.html")
    
@permission_required('matchups.add_matchup')
def select_tie_breaker_matchups(request):
    tie_breaker_list = list()
    if request.method == 'POST':
        for week_number in range(1, week_number_for_last_matchup()):
            field_name = str(week_number)+'-matchup_field'
            selected_tie_breaker = request.POST[field_name]
            set_tie_breaker_for_week(week_number, selected_tie_breaker)
    for week_number in range(1, week_number_for_last_matchup()):
        matchups, tie_breaker = matchups_for_week(week_number)
        form = SelectTieBreakerForm(matchups, tie_breaker, prefix=week_number)
        tie_breaker_list.append(TieBreakerFormToCurrentValue(form, tie_breaker))
    content = {'tie_breaker_list':tie_breaker_list}
    return render(request, "select_tie_breaker_matchups.html", content)

def set_tie_breaker_for_week(week_number, selected_tie_breaker):
    matchups, tie_breaker = matchups_for_week(week_number)
    if tie_breaker:
        tie_breaker.delete()
    if selected_tie_breaker:
        matchup = Matchup.objects.get(id=selected_tie_breaker)
        new_tie_breaker = TieBreaker(matchup=matchup)
        new_tie_breaker.save()
        
class TieBreakerFormToCurrentValue:
    form = None
    current_value = None
    def __init__(self, form, current_value):
        self.form = form
        self.current_value = current_value

class SelectTieBreakerForm(forms.Form):
    matchup_field = forms.ChoiceField()
    def __init__(self, matchups, tie_breaker, *args, **kwargs):        
        super(SelectTieBreakerForm, self).__init__(*args, **kwargs)
        matchup_list = list()
        widget_choices = list()
        widget_choices.append(('',''))
        for matchup in matchups:
            matchup_list.append(matchup)
            widget_choices.append((matchup.id, matchup.full_name()))
        if tie_breaker:
            matchup_list.append(tie_breaker)
            widget_choices.append((tie_breaker.id, tie_breaker.full_name()))
        self.fields['matchup_field'].widget.choices = widget_choices