from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect, reverse, get_object_or_404
from django.template import loader, Context
from .render_block import render_block_to_string
from django.http import HttpResponse
from datetime import datetime, timezone
import ast
from time import sleep
from django import db
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

#add_to_end: 2017-08-21 12:45:24.934096
from django.db import models
from django.views import generic
import numpy as np
from .models import mt_game, mt_deck, mt_player, mt_iq
from decimal import *

def login(request):
	return render(
		request,
		'login.html'
	)

def base_generic(request):
	return render(
		request,
		'base_generic.html'
	)
#add_to_end: 2017-08-21 12:45:24.934154

def home(request):
	games_list = mt_game.objects.filter(f_player2=request.user, f_p1_waiting=1).values()
	user = str(request.user).strip()
	priv_users = ["sharan","bhava","saru","shar","admin", "superadmin"]
	
	context = {'games_list':games_list, 'user':user, 'priv_users':priv_users}
	return render(
		request,
		'home.html',
		context
	)

def game2_play(request):
	if request.method == "POST":
		user = request.user
		id = int(request.POST.get("id"))
		game=get_object_or_404(mt_game, pk=id)
		card_deck = [['carr','drag','ghos','spot','bomb','excl','ques','clow'], ['keyz','sunz','cand','tort','snow','moon','carr','yiny'], ['spot','penc','dogz','stop','scis','drag','webz','keyz'], ['chee','sung','musi','catz','dino','skul','moon','drag'], ['spid','excl','appl','scis','mapl','snof','moon','iglo'], ['tort','drag','chic','appl','anch','bugz','dino','ghos'], ['carr','potz','chic','icec','iglo','bulb','musi','stop'], ['musi','flow','excl','lipz','anch','carz','lock','keyz'], ['spot','potz','skul','snof','cook','leaf','cand','anch'], ['carz','chee','snow','bott','spot','dolp','iglo','fire'], ['skul','hear','carz','penc','carr','bolt','cact','appl'], ['snow','potz','tree','catz','webz','appl','bomb','lock'], ['carz','yiny','hors','bomb','bulb','targ','dino','snof'], ['chee','cact','spid','potz','dogz','yiny','lipz','ghos'], ['flow','penc','clow','potz','moon','hors','fire','bugz'], ['cloc','yiny','lock','skul','icec','clow','scis','dolp'], ['hors','webz','cloc','carr','anch','chee','mapl','hamm'], ['ques','hear','stop','chee','snof','sunz','bugz','lock'], ['bolt','excl','drop','dino','potz','sunz','bott','cloc'], ['eyez','zebr','carr','lock','leaf','fire','dino','spid'], ['catz','lipz','cook','targ','bott','scis','bugz','carr'], ['ques','potz','sung','carz','scis','zebr','hamm','tort'], ['spot','tree','zebr','bolt','yiny','musi','mapl','bugz'], ['excl','cact','hors','catz','cand','stop','dolp','zebr'], ['ques','dogz','targ','fire','appl','cloc','cand','musi'], ['cook','excl','sung','yiny','chic','hear','fire','webz'], ['cloc','penc','chic','drag','zebr','snow','snof','lipz'], ['flow','dogz','sung','dolp','tree','drop','carr','snof'], ['targ','potz','hear','eyez','keyz','mapl','dolp','drag'], ['stop','appl','bott','flow','yiny','drag','leaf','hamm'], ['eyez','clow','cact','musi','webz','tort','snof','bott'], ['snow','hear','drop','scis','ghos','leaf','musi','hors'], ['penc','sung','lock','ghos','mapl','bulb','cand','bott'], ['skul','drop','lipz','mapl','stop','bomb','fire','tort'], ['eyez','ques','penc','catz','drop','yiny','iglo','anch'], ['carz','drop','webz','spid','cand','drag','icec','bugz'], ['clow','drop','keyz','chee','bulb','zebr','cook','appl'], ['spot','hear','cloc','flow','bulb','catz','spid','tort'], ['sung','cact','keyz','leaf','bomb','cloc','bugz','iglo'], ['hear','dogz','zebr','moon','bomb','anch','icec','bott'], ['targ','ghos','webz','flow','zebr','sunz','skul','iglo'], ['penc','sunz','cook','hamm','musi','dolp','spid','bomb'], ['spot','eyez','sung','icec','sunz','hors','lipz','appl'], ['tree','sunz','bulb','cact','anch','drag','scis','fire'], ['chee','excl','penc','tort','targ','leaf','tree','icec'], ['snow','clow','targ','sung','stop','spid','bolt','anch'], ['hamm','clow','hear','tree','iglo','drag','cand','lipz'], ['chic','tree','hors','ques','skul','keyz','spid','bott'], ['eyez','ghos','carz','tree','cook','moon','cloc','stop'], ['eyez','chic','cand','flow','chee','bomb','scis','bolt'], ['ghos','keyz','snof','catz','hamm','icec','fire','bolt'], ['lock','iglo','dogz','hors','drag','cook','bolt','tort'], ['clow','carz','chic','catz','leaf','dogz','sunz','mapl'], ['dolp','ques','webz','moon','leaf','lipz','bolt','bulb'], ['chic','cact','drop','lock','targ','spot','moon','hamm']]
		set1 = game.f_set1
		set2 = game.f_set2
		set1 = ast.literal_eval(set1)
		set2 = ast.literal_eval(set2)
		if request.POST.get("type") == "first":
			key_card_no = int(game.f_key)
			first1 = int(set1[0])
			first2 = int(set2[0])
			if str(request.user).strip() == game.f_player1:
				player_ready = game.f_p2_waiting
				context = {'user':user, 'game':game, 'key':key_card_no, 'set1':set1, 'set2':set2, 'play_card_no':first1, 'key_card':card_deck[key_card_no], 'play_card':card_deck[first1]}
			elif str(request.user).strip() == game.f_player2:
				player_ready = game.f_p1_waiting
				context = {'user':user, 'game':game, 'key':key_card_no, 'set1':set1, 'set2':set2, 'play_card_no':first2, 'key_card':card_deck[key_card_no], 'play_card':card_deck[first2]}
			else:
				return HttpResponse()
			while player_ready < 1:
				if str(request.user).strip() == game.f_player1:
					player_ready = mt_game.objects.get(id = id).f_p2_waiting
				if str(request.user).strip() == game.f_player2:
					player_ready = mt_game.objects.get(id = id).f_p1_waiting
				sleep(1)
			if str(request.user).strip() == game.f_player1:
				mt_game.objects.filter(pk=id).update(f_p1_started=1, f_p1_waiting=2, f_p1_start_time = datetime.now())
			if str(request.user).strip() == game.f_player2:
				mt_game.objects.filter(pk=id).update(f_p2_started=1, f_p2_waiting=2, f_p2_start_time = datetime.now())
			db.connections.close_all()
			return render(
				request,
				'game2.html',
				context
			)
		elif request.POST.get("type") == "second":
			play = game.f_play
			play = ast.literal_eval(play)
			last = int(play[-1])
			key_card_no = int(request.POST.get("key_card_no"))
			play_card_no = int(request.POST.get("play_card_no"))
			if str(request.user).strip() == game.f_player1:
				if game.f_p2_stopped == 1:
					mt_game.objects.filter(pk=id).update(f_p1_stopped=1)
					return render(request, 'game2_end.html', {'user_var':user, 'id_var': id, 'result':"lose", 'cards_left':len(set1) - game.f_p1_cards_played})
			elif str(request.user).strip() == game.f_player2:
				if game.f_p1_stopped == 1:
					mt_game.objects.filter(pk=id).update(f_p2_stopped=1)
					return render(request, 'game2_end.html', {'user_var':user, 'id_var': id, 'result':"lose", 'cards_left':len(set2) - game.f_p2_cards_played})
			else:
				return HttpResponse()
			if key_card_no == last:
				play.append(play_card_no)
				mt_game.objects.filter(pk=id).update(f_play=play)
				game.f_play = play
				#return render(request, 'game2_end.html', {'user_var':user, 'id_var': id, 'p1_time_var':request.user, 'p2_time_var':game.f_player1})
				if str(request.user).strip() == game.f_player1:
					if play_card_no == int(set1[-1]):
						t = (datetime.now(timezone.utc) - game.f_p1_start_time).seconds
						mt_game.objects.filter(pk=id).update(f_p1_stopped=1, f_p1_cards_played = game.f_p1_cards_played + 1, f_winner = str(request.user).strip(), f_p1_play_time = t)
						return render(request, 'game2_end.html', {'user_var':user, 'id_var': id, 'result':"win", 'cards_left':len(set2) - game.f_p2_cards_played, 'play_time': t})
					ind1 = set1.index(play_card_no)
					next_card_no = set1[ind1 + 1]
					mt_game.objects.filter(pk=id).update(f_p1_cards_played = game.f_p1_cards_played + 1)
					context = {'user':user, 'game':game, 'key':play_card_no, 'set1':set1, 'set2':set2, 'play_card_no':next_card_no, 'key_card':card_deck[play_card_no], 'play_card':card_deck[next_card_no]}
					return render(request, 'game2.html', context)
				elif str(request.user).strip() == game.f_player2:
					if play_card_no == int(set2[-1]):
						t = (datetime.now(timezone.utc) - game.f_p2_start_time).seconds
						mt_game.objects.filter(pk=id).update(f_p2_stopped=1, f_p2_cards_played = game.f_p2_cards_played + 1, f_winner = str(request.user).strip(), f_p2_play_time = t)
						return render(request, 'game2_end.html', {'user_var':user, 'id_var': id, 'result':"win", 'cards_left':len(set1) - game.f_p1_cards_played, 'play_time': t})
					ind2 = set2.index(play_card_no)
					next_card_no = set2[ind2 + 1]
					mt_game.objects.filter(pk=id).update(f_p2_cards_played = game.f_p2_cards_played + 1)
					context = {'user':user, 'game':game, 'key':play_card_no, 'set1':set1, 'set2':set2, 'play_card_no':next_card_no, 'key_card':card_deck[play_card_no], 'play_card':card_deck[next_card_no]}
					return render(request, 'game2.html', context)
			else:
				if str(request.user).strip() == game.f_player1:
					context = {'user':user, 'game':game, 'key':last, 'set1':set1, 'set2':set2,  'play_card_no':play_card_no, 'key_card':card_deck[last], 'play_card':card_deck[play_card_no]}
					return render(request, 'game2.html', context)
				elif str(request.user).strip() == game.f_player2:
					context = {'user':user, 'game':game, 'key':last, 'set1':set1, 'set2':set2, 'play_card_no':play_card_no, 'key_card':card_deck[last], 'play_card':card_deck[play_card_no]}
					return render(request, 'game2.html', context)
		elif request.method == "POST" and request.POST.get("type") == "third":
			play = game.f_play
			play = ast.literal_eval(play)
			last = int(play[-1])
			key_card_no = int(request.POST.get("key_card_no"))
			play_card_no = int(request.POST.get("play_card_no"))
			time_now1 = datetime.now()
			time_now2 = datetime.now()
			while last == key_card_no and (time_now2-time_now1).seconds < 10:
				game = get_object_or_404(mt_game, pk=id)
				play = game.f_play
				play = ast.literal_eval(play)
				last = int(play[-1])
				sleep(0.1)
			if last != key_card_no:
				context = {'user':user, 'game':game, 'key':last, 'set1':set1, 'set2':set2, 'play_card_no':play_card_no, 'key_card':card_deck[last], 'play_card':card_deck[play_card_no]}
			else:
				context = {'user':user, 'game':game, 'key':key_card_no, 'set1':set1, 'set2':set2, 'play_card_no':play_card_no, 'key_card':card_deck[key_card_no], 'play_card':card_deck[play_card_no]}
			return render(request, 'game2.html', context)
		else:
			return HttpResponse()
	else:
		return HttpResponse()

from .forms import CreateForm

def create(request):
	if request.method == "POST":
		form = CreateForm(request.POST)
		if form.is_valid():
			full = list(range(0,54))
			shuffle = np.random.choice(full, 54, replace=False)
			key = shuffle[0]
			set1 = list(shuffle[1:21])
			set2 = list(shuffle[21:41])
			post = form.save(commit=False)
			post.f_player1 = request.user
			post.f_key = key
			post.f_set1 = set1
			post.f_set2 = set2
			post.f_play = [key]
			post.published_date = datetime.now()
			post.save()
			return redirect('wait', post.id)
	else:
		form = CreateForm()
	return render(request, 'create.html', {'form': form})
	
def wait(request, pk):
	user = request.user
	game=get_object_or_404(mt_game, pk=pk)
	if str(request.user).strip() == game.f_player1:
		mt_game.objects.filter(pk=pk).update(f_p1_waiting=1)
	if str(request.user).strip() == game.f_player2:
		mt_game.objects.filter(pk=pk).update(f_p2_waiting=1)
	context = {'user':user, 'id':pk}
	return render(request, 'wait.html', context)
	

def join(request):
	return render(
		request,
		'join.html'
	)

def game2_end(request):
	if request.method == "POST":
		if request.POST.get("type") == "first":
			user_var = request.POST.get("user")
			id_var = int(request.POST.get("id"))
			game=get_object_or_404(mt_game, pk=id_var)
			if str(request.user).strip() == game.f_player1:
				p1_time_var = int(request.POST.get("time"))
				p2_time_var = game.f_p2_play_time
				mt_game.objects.filter(pk=id_var).update(f_p1_play_time=p1_time_var)
				return render(request, 'game2_end.html', {'user_var':user_var, 'id_var': id_var, 'p1_time_var':p1_time_var, 'p2_time_var':p2_time_var})
			elif str(request.user).strip() == game.f_player2:
				p1_time_var = game.f_p1_play_time
				p2_time_var = int(request.POST.get("time"))
				mt_game.objects.filter(pk=id_var).update(f_p2_play_time=p2_time_var)
				return render(request, 'game2_end.html', {'user_var':user_var, 'id_var': id_var, 'p1_time_var':p2_time_var, 'p2_time_var':p1_time_var})
		elif request.POST.get("type") == "second":
			user_var = request.user
			id_var = int(request.POST.get("id"))
			game=get_object_or_404(mt_game, pk=id_var)
			p1_time_var = game.f_p1_play_time
			p2_time_var = game.f_p2_play_time
			time_now1 = datetime.now()
			time_now2 = datetime.now()
			if str(request.user).strip() == game.f_player1:
				while p2_time_var == 0 and (time_now2-time_now1).seconds < 10:
					p2_time_var = mt_game.objects.get(id = id_var).f_p2_play_time
					time_now2 = datetime.now()
				return render(request, 'game2_end.html', {'user_var':user_var, 'id_var': id_var, 'p1_time_var':p1_time_var, 'p2_time_var':p2_time_var})
			elif str(request.user).strip() == game.f_player2:
				while p1_time_var == 0 and (time_now2-time_now1).seconds < 10:
					p1_time_var = mt_game.objects.filter(id = id_var).values_list('f_p1_play_time')
					time_now2 = datetime.now()
				return render(request, 'game2_end.html', {'user_var':user_var, 'id_var': id_var, 'p1_time_var':p2_time_var, 'p2_time_var':p1_time_var})
			else:
				return HttpResponse()
		else:
			return HttpResponse()
	return HttpResponse()

def bad_boxes(request):
	return render(
		request,
		'bad_boxes.html'
	)

def iq(request):
	return render(
		request,
		'iq.html'
	)
	
def iq_end(request):
	if request.method == "POST":
		if request.POST.get("type") == "first":
			user_var = str(request.user).strip()
			play_time = Decimal(request.POST.get("play_time"))
			#id_var = int(request.POST.get("id"))
			#game=get_object_or_404(mt_game, pk=id_var)
			try:
				game = mt_player.objects.get(f_player_name=user_var)
				game.f_g_iq_avg_time = ((game.f_g_iq_avg_time * game.f_g_iq_no_games) + play_time) / (game.f_g_iq_no_games + 1)
				game.f_g_iq_no_games = game.f_g_iq_no_games + 1
				if play_time < game.f_g_iq_best_time:
					game.f_g_iq_best_time = play_time
					best_time = round(play_time,2)
				else:
					best_time = game.f_g_iq_best_time
				avg_time = round(game.f_g_iq_avg_time,2)
				game.save()
			except ObjectDoesNotExist:
				game = mt_player(f_player_name=user_var, f_g_iq_avg_time=play_time, f_g_iq_best_time=play_time, f_g_iq_no_games=1)
				best_time = round(play_time,2)
				avg_time = round(play_time,2)
				game.save()
			gam = mt_iq(f_player=user_var,f_play_time=play_time)
			gam.save()
			return render(request, 'iq_end.html', {'user_var':user_var, 'play_time':play_time, 'avg_time':avg_time, 'best_time':best_time})
		else:
			return HttpResponse()
	return HttpResponse()