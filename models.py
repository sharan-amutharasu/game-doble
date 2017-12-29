from django.db import models

# Create your models here.

#add_to_end: 2017-08-24 08:42:19.063507
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances
from django.contrib.auth.models import User
from datetime import datetime

#add_to_end: 2017-08-24 08:45:15.134057

#model:mt_game
class mt_game(models.Model):

	#mt_ball.fields
	f_game_name = models.CharField(primary_key=False, max_length=100, default="dgame")
	f_game_size = models.IntegerField(default = 2)
	f_game_password = models.CharField(max_length = 20, default="password")
	f_player1 = models.CharField(max_length=100)
	f_player2 = models.CharField(max_length=100)
	f_player3 = models.CharField(max_length=100)
	f_p1_start_time = models.DateTimeField(default = datetime.now)
	f_p2_start_time = models.DateTimeField(default = datetime.now)
	f_p3_start_time = models.DateTimeField(default = datetime.now)
	f_p1_play_time = models.IntegerField(default = 0)
	f_p2_play_time = models.IntegerField(default = 0)
	f_p3_play_time = models.IntegerField(default = 0)
	f_p1_waiting = models.IntegerField(default = 0)
	f_p2_waiting = models.IntegerField(default = 0)
	f_p3_waiting = models.IntegerField(default = 0)
	f_p1_started = models.IntegerField(default = 0)
	f_p2_started = models.IntegerField(default = 0)
	f_p3_started = models.IntegerField(default = 0)
	f_p1_stopped = models.IntegerField(default = 0)
	f_p2_stopped = models.IntegerField(default = 0)
	f_p3_stopped = models.IntegerField(default = 0)
	f_p1_cards_played = models.IntegerField(default = 0)
	f_p2_cards_played = models.IntegerField(default = 0)
	f_p3_cards_played = models.IntegerField(default = 0)
	f_key = models.CharField(max_length=100, default="none")
	f_set1 = models.CharField(max_length=100, default="none")
	f_set2 = models.CharField(max_length=100, default="none")
	f_set3 = models.CharField(max_length=100, default="none")
	f_play = models.CharField(max_length=100, default="none")
	f_winner = models.CharField(max_length=100, default="none")

	#mt_ball.meta
	class Meta: 
		ordering = ['f_game_name']

	#mt_ball.methods
	def get_absolute_url(self):
		 return reverse('game2', args=[str(self.id)])

	def __str__(self):
		return self.f_game_name


#add_to_end: 2017-08-24 08:45:15.134090

#model:mt_deck
class mt_deck(models.Model):

	#mt_deck.fields
	f_card_no = models.IntegerField(primary_key=True)
	f_e1 = models.CharField(max_length=100)
	f_e2 = models.CharField(max_length=100)
	f_e3 = models.CharField(max_length=100)
	f_e4 = models.CharField(max_length=100)
	f_e5 = models.CharField(max_length=100)
	f_e6 = models.CharField(max_length=100)
	f_e7 = models.CharField(max_length=100)
	f_e8 = models.CharField(max_length=100)
	f_e1_size = models.IntegerField()
	f_e2_size = models.IntegerField()
	f_e3_size = models.IntegerField()
	f_e4_size = models.IntegerField()
	f_e5_size = models.IntegerField()
	f_e6_size = models.IntegerField()
	f_e7_size = models.IntegerField()
	f_e8_size = models.IntegerField()

	#mt_ball.meta
	class Meta: 
		ordering = ['f_card_no']

	#mt_ball.methods
	def get_absolute_url(self):
		 return reverse('mt_deck', args=[str(self.f_card_no)])

	def __str__(self):
		return str(self.f_card_no)
		
	def list_elements(self):
		return [self.f_e1, self.f_e2, self.f_e3, self.f_e4, self.f_e5, self.f_e6, self.f_e7, self.f_e8]

		

#model:mt_iq
class mt_iq(models.Model):

	#mt_ball.fields
	f_game_name = models.CharField(primary_key=False, max_length=100, default="dgame")
	f_player = models.CharField(max_length=100)
	f_time = models.DateTimeField(default = datetime.now)
	f_play_time = models.DecimalField(default = 0, max_digits = 10, decimal_places = 3)

	#mt_ball.meta
	class Meta: 
		ordering = ['f_game_name']

	#mt_ball.methods
	def get_absolute_url(self):
		 return reverse('mt_iq', args=[str(self.id)])

	def __str__(self):
		return self.f_game_name


#model:mt_player
class mt_player(models.Model):

	#mt_ball.fields
	f_player_name = models.CharField(primary_key=False, max_length=100, default="player")
	f_g_iq_avg_time = models.DecimalField(default = 0, max_digits = 10, decimal_places = 3)
	f_g_iq_best_time = models.DecimalField(default = 0, max_digits = 10, decimal_places = 3)
	f_g_iq_no_games = models.IntegerField(default = 1)

	#mt_ball.meta
	class Meta: 
		ordering = ['f_player_name']

	#mt_ball.methods
	def get_absolute_url(self):
		 return reverse('mt_player', args=[str(self.id)])

	def __str__(self):
		return self.f_player_name
