from django.contrib import admin
from .models import mt_game, mt_deck, mt_player, mt_iq

# Register your models here.
admin.site.register(mt_game)
admin.site.register(mt_deck)
admin.site.register(mt_player)
admin.site.register(mt_iq)