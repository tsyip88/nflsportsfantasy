from django.contrib import admin
from matchups.models import Matchup, Pick, TieBreaker, TieBreakerPick

admin.site.register(Matchup)
admin.site.register(Pick)
admin.site.register(TieBreaker)
admin.site.register(TieBreakerPick)