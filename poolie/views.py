from django.shortcuts import render, redirect
from django import forms
import django.contrib.auth
from django.contrib.auth.decorators import permission_required
import matchups.matchup_data_retriever
import teams.team_data_retriever
import teams.models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length = 50, widget=forms.PasswordInput)

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
    if request.user.is_authenticated():
        logged_in = True
    else:
        logged_in = False
    context = {'logged_in': logged_in}
    return render(request, "index.html", context)

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
            teams = teams.models.Team.objects.all()
            for team in teams:
                team.image_location = team.full_name().replace(' ','').replace('.','') + '.png'
                team.save()
    return render(request, "admin_actions.html")