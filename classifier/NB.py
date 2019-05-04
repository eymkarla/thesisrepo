import math
from copy import deepcopy
from dictionary.models import Language
import nltk


class NaiveBayes:

	def my_count(self, *args):
		waray_count = {}
		cebuano_count = {}
		hiligaynon_count = {}
		sentence = args[0].lower().split(' ')
		for item in sentence:
			waray_count[item] = Language.objects.filter(dialect='Waray', word=item).count()
		for item in sentence:
			cebuano_count[item] = Language.objects.filter(dialect='Cebuano', word=item).count()
		for item in sentence:
			hiligaynon_count[item] = Language.objects.filter(dialect='Hiligaynon', word=item).count()
		
		return waray_count, cebuano_count, hiligaynon_count

	def dcount(self, args):
		total = 0
		for items in args:
			for i in items.values():
				total = total + i

		return total

			
	def train(self, total):
		self.features = {}
		self.features['warFeatures'] = {}
		self.features['cebFeatures'] = {}
		self.features['hilFeatures'] = {}

		self.priorLogWar = math.log(self.waray_count/self.total)
		self.priorLogCeb = math.log(self.cebu_count/self.total)
		self.priorLogHil = math.log(self.hili_count/self.total)

			for sentence, count in self.warays.items():
				self.features['warFeatures'][sentence] = math.log((count + 1)/(self.waray_count + self.total))
			
			for sentence, count in self.cebus.items():
				self.features['cebFeatures'][sentence] = math.log((count + 1)/(self.cebu_count + self.total))

			for sentence, count in self.hiligs.items():
				self.features['hilFeatures'][sentence] = math.log((count + 1)/(self.hili_count + self.total))

	def testing(self, word):
		caller = word
		war_val = self.priorLogWar
		ceb_val = self.priorLogCeb
		hil_val = self.priorLogHil
		context = {}

		smooth_war = math.log(1/(self.waray_count + self.doc_count))
		smooth_ceb = math.log(1/(self.cebu_count + self.doc_count))
		smooth_hil = math.log(1/(self.hili_count + self.doc_count))

		for feature in self.features:
			if feature == 'warFeatures':
				for sentence in caller:
					if sentence in self.features['warFeatures']:
						war_val += self.features['warFeatures'][sentence]
					elif sentence in self.features['cebFeatures'] or self.features['hilFeatures']:
						war_val += smooth_war
			elif feature == 'cebFeatures':
				for sentence in caller:
					if sentence in self.features['cebFeatures']:
						ceb_val += self.features['cebFeatures'][sentence]
					elif sentence in self.features['warFeatures'] or self.features['hilFeatures']:
						ceb_val += smooth_ceb
			elif feature == 'hilFeatures':
				for sentence in caller:
					if sentence in self.features['hilFeatures']:
						hil_val += self.features['hilFeatures'][sentence]
					elif sentence in self.features['warFeatures'] or self.features['cebFeatures']:
						hil_val += smooth_hil
		if war_val > ceb_val and war_val > hil_val:
			print('waray')
		elif ceb_val >  war_val and ceb_val > hil_val:
			print('cebuano')
		elif hil_val > war_val and hil_val > ceb_val:
			print('hiligaynon')
		else:
			print ('The Classification Result')
				
