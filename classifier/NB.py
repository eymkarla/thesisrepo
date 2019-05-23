import math
import nltk
nltk.download('stopwords')
import pandas as pd
import re
from copy import deepcopy
from dictionary.models import Dialect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from django.shortcuts import render, redirect

class NaiveBayes:

	def split_reg(self, *args):
		sentence = self.lower()

		new = ' '.join([word for word in re.split(r'[^A-Za-z]', sentence) if word])

		return new

	def split_word(new):
		stop_words_lst = set(stopwords.words("english"))
		stop_words_lst.update (('ako','ang','amua','ato','busa','ikaw','ila','ilang','imo','imong','iya','iyang','kaayo','kana',
'kaniya','kaugalingon','kay','kini','kinsa','kita','lamang','mahimong','mga','mismo','nahimo'
,'nga','pareho','pud','sila','siya','unsa','sa','ug','nang', 'ng','diay', 'atu', 'mo'))
		sentence = new.lower()

		new_str = ' '.join([word for word in sentence.split(' ') if word not in stop_words_lst]) 

		return new_str

		
	def train_waray(new_str):
		waray_count = Dialect.objects.filter(dialect='Waray').count()
		doc_count = Dialect.objects.count()
		warays = Dialect.objects.filter(dialect='Waray')
		sentence = new_str.lower()
		user_inputs = sentence.split(' ')
		war_count = 1

		for waray in warays:
			for user_input in user_inputs:
				if waray.word == user_input:
					war_count *= (1 + 1) / (waray_count + doc_count)

		return war_count
	
	def train_cebuano(new_str):
		cebu_count = Dialect.objects.filter(dialect='Cebuano').count()
		doc_count = Dialect.objects.count()
		cebus = Dialect.objects.filter(dialect='Cebuano')
		sentence = new_str.lower()
		user_inputs = sentence.split(' ')
		ceb_count = 1

		for cebu in cebus:
			for user_input in user_inputs:
				if cebu.word == user_input:
					ceb_count *= (1 + 1) / (cebu_count + doc_count)

		return ceb_count

	def train_hiligaynon(new_str):
		hili_count = Dialect.objects.filter(dialect='Hiligaynon').count()
		doc_count = Dialect.objects.count()
		hiligs = Dialect.objects.filter(dialect='Hiligaynon')
		sentence = new_str.lower()
		user_inputs = sentence.split(' ')
		hil_count = 1

		for hilig in hiligs:
			for user_input in user_inputs:
				if hilig.word == user_input:
					hil_count *= (1 + 1) / (hili_count + doc_count)

		return hil_count

	def smooth_waray(new_str):
		waray_count = Dialect.objects.filter(dialect='Waray').count()
		doc_count = Dialect.objects.count()
		sentence = new_str.lower()
		user_inputs = sentence.split(' ')
		smooth_war = 1

		for items in user_inputs:
			if Dialect.objects.filter(word=items, dialect='Waray').exists():
				pass
			else:
				smooth_war *= 1 / (waray_count + doc_count)

		return smooth_war

	def smooth_cebuano(new_str):
		cebu_count = Dialect.objects.filter(dialect='Cebuano').count()
		doc_count = Dialect.objects.count()
		sentence = new_str.lower()
		user_inputs = sentence.split(' ')
		smooth_ceb = 1

		for items in user_inputs:
			if Dialect.objects.filter(word=items, dialect='Cebuano').exists():
				pass
			else:
				smooth_ceb *= 1 / (cebu_count + doc_count)

		return smooth_ceb

	def smooth_hiligaynon(new_str):
		hili_count = Dialect.objects.filter(dialect='Hiligaynon').count()
		doc_count = Dialect.objects.count()
		sentence = new_str.lower()
		user_inputs = sentence.split(' ')
		smooth_hil = 1
		
		for items in user_inputs:
			if Dialect.objects.filter(word=items, dialect='Hiligaynon').exists():
				pass
			else:
				smooth_hil *= 1 / (hili_count + doc_count)

		return smooth_hil

	def multi_words(war_count, ceb_count, hil_count, smooth_war, smooth_ceb, smooth_hil):
		waray_count = Dialect.objects.filter(dialect='Waray').count()
		cebu_count = Dialect.objects.filter(dialect='Cebuano').count()
		hili_count = Dialect.objects.filter(dialect='Hiligaynon').count()
		doc_count = Dialect.objects.count()
		
		priorLogWar = waray_count/doc_count
		priorLogCeb = cebu_count/doc_count
		priorLogHil = hili_count/doc_count

		war_val = 0
		ceb_val = 0
		hil_val = 0


		if war_count == 1:
			war_val *= war_count
		else:
			war_val = war_count * smooth_war * priorLogWar

		if ceb_count == 1:
			ceb_val *= ceb_count
		else:
			ceb_val = ceb_count * smooth_ceb * priorLogCeb

		if hil_count == 1:
			hil_val *= hil_count
		else:
			hil_val = hil_count * smooth_hil * priorLogHil
		
		
		if war_val > ceb_val and war_val > hil_val:
			return 'Waray'
		elif ceb_val > war_val and ceb_val > hil_val:
			return 'Cebuano'
		elif hil_val > war_val and hil_val > ceb_val:
			return 'Hiligaynon'
		elif war_val and ceb_val and hil_val == 0:
			return 'Word does not exist'