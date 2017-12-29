from django import forms
from .models import mt_game
	
class CreateForm(forms.ModelForm):


    class Meta:
        model = mt_game
        fields = ['f_game_name','f_game_size','f_player2']
        labels = { 'f_game_name': ('Game Name'), 'f_game_size': ('Number of players'), 'f_player2': ('Other player username')}