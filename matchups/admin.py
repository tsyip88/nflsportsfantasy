from django.contrib import admin
from matchups.models import Matchup, Pick, TieBreaker

admin.site.register(Matchup)
admin.site.register(Pick)
admin.site.register(TieBreaker)