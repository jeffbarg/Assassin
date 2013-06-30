from django.contrib import admin

from games.models import Game

class GameAdmin(admin.ModelAdmin):
	pass

admin.site.register(Game, GameAdmin)