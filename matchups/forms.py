import matchups.models
from django import forms

class PickForm(forms.ModelForm):
    class Meta:
        model = matchups.models.Pick
        fields = {'selected_team'}
        widgets = {'selected_team': forms.RadioSelect()}
    def __init__(self, *args, **kwargs):
        super(PickForm, self).__init__(*args, **kwargs)
        widget_choices = []
        if self.instance.matchup_id:
            if self.instance.matchup:
                matchup = self.instance.matchup
                if matchup.id and \
                   matchup.home_team_id and \
                   matchup.away_team_id:
                    away_team = matchup.away_team
                    home_team = matchup.home_team
                    widget_choices.append((away_team.id, away_team.full_name()))
                    widget_choices.append((home_team.id, home_team.full_name()))
                    self.fields['selected_team'].widget.choices = widget_choices
                    matchup_label = matchup.date_time_string() + ' - ' \
                                    + away_team.full_name() + ' at ' \
                                    + home_team.full_name()
                    self.fields['selected_team'].label = matchup_label
                    
class TieBreakerForm(forms.ModelForm):
    predicted_total_score = forms.CharField(label='Tie breaker')
    class Meta:
        model = matchups.models.TieBreakerPick
        fields = {'predicted_total_score'}