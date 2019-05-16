import math
import re
import pandas as pd
from copy import deepcopy
from dictionary.models import Language


class NaiveBayes:

			
	def train_waray(self, *args):
		waray_count = Language.objects.filter(dialect='Waray').count()
		doc_count = Language.objects.count()
		warays = Language.objects.filter(dialect='Waray')
		sentence = self.lower()
		user_inputs = sentence.split("stop_words", ' ')
		stop_words = ["ako","amua","ato","busa","ikaw","ila","ilang","imo","imong","iya","iyang","kaayo",
		"kana","kaniya","kaugalingon","kay","kini","kinsa","kita","lamang","mahimong","mga","mismo","nahimo",
		"nga","pareho","pud","sila","siya","unsa","sa","ug","nang", "ng","diay", "atu"]
		war_count = 1

		for waray in warays:
			for user_input in user_inputs:
				if waray.word == user_input:
					war_count *= (1 + 1) / (waray_count + doc_count)
		import pdb; pdb.set_trace()
		return war_count
	
	def train_cebuano(self, *args):
		cebu_count = Language.objects.filter(dialect='Cebuano').count()
		doc_count = Language.objects.count()
		cebus = Language.objects.filter(dialect='Cebuano')
		sentence = self.lower()
		user_inputs = sentence.split(' ')
		ceb_count = 1

		for cebu in cebus:
			for user_input in user_inputs:
				if cebu.word == user_input:
					ceb_count *= (1 + 1) / (cebu_count + doc_count)

		return ceb_count

	def train_hiligaynon(self, *args):
		hili_count = Language.objects.filter(dialect='Hiligaynon').count()
		doc_count = Language.objects.count()
		hiligs = Language.objects.filter(dialect='Hiligaynon')
		sentence = self.lower()
		user_inputs = sentence.split(' ')
		hil_count = 1

		for hilig in hiligs:
			for user_input in user_inputs:
				if hilig.word == user_input:
					hil_count *= (1 + 1) / (hili_count + doc_count)

		return hil_count

	def smooth_waray(self, *args):
		waray_count = Language.objects.filter(dialect='Waray').count()
		doc_count = Language.objects.count()
		sentence = self.lower()
		user_inputs = sentence.split(' ')
		smooth_war = 1

		for items in user_inputs:
			if Language.objects.filter(word=items, dialect='Waray').exists():
				pass
			else:
				smooth_war *= 1 / (waray_count + doc_count)

		return smooth_war

	def smooth_cebuano(self, *args):
		cebu_count = Language.objects.filter(dialect='Cebuano').count()
		doc_count = Language.objects.count()
		sentence = self.lower()
		user_inputs = sentence.split(' ')
		smooth_ceb = 1

		for items in user_inputs:
			if Language.objects.filter(word=items, dialect='Cebuano').exists():
				pass
			else:
				smooth_ceb *= 1 / (cebu_count + doc_count)

		return smooth_ceb

	def smooth_hiligaynon(self, *args):
		hili_count = Language.objects.filter(dialect='Hiligaynon').count()
		doc_count = Language.objects.count()
		sentence = self.lower()
		user_inputs = sentence.split(' ')
		smooth_hil = 1
		
		for items in user_inputs:
			if Language.objects.filter(word=items, dialect='Hiligaynon').exists():
				pass
			else:
				smooth_hil *= 1 / (hili_count + doc_count)

		return smooth_hil

	def multi_words(war_count, ceb_count, hil_count, smooth_war, smooth_ceb, smooth_hil):
		waray_count = Language.objects.filter(dialect='Waray').count()
		cebu_count = Language.objects.filter(dialect='Cebuano').count()
		hili_count = Language.objects.filter(dialect='Hiligaynon').count()
		doc_count = Language.objects.count()
		
		priorLogWar = waray_count/doc_count
		priorLogCeb = cebu_count/doc_count
		priorLogHil = hili_count/doc_count

		war_val = war_count * smooth_war
		ceb_val = ceb_count * smooth_ceb
		hil_val = hil_count * smooth_hil

		
		if war_val > ceb_val and war_val > hil_val:
			print("Waray")
		elif ceb_val > war_val and ceb_val > hil_val:
			print("Cebuano")
		elif hil_val > war_val and hil_val > ceb_val:
			print("Hiligaynon")

		# import pdb; pdb.set_trace()