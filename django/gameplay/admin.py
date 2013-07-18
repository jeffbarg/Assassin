from django.contrib import admin

from gameplay.models import GameSession

class GameSessionAdmin(admin.ModelAdmin):
	pass

admin.site.register(GameSession, GameSessionAdmin)