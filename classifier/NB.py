import math
from copy import deepcopy
from dictionary.models import Language


class NaiveBayes:
			
	def train(self, *args):
		waray_count = Language.objects.filter(dialect='Waray').count()
		cebu_count = Language.objects.filter(dialect='Cebuano').count()
		hili_count = Language.objects.filter(dialect='Hiligaynon').count()
		doc_count = Language.objects.count()
		warays = Language.objects.filter(dialect='Waray')
		hiligs = Language.objects.filter(dialect='Hiligaynon')
		cebus = Language.objects.filter(dialect='Cebuano')
		sentence = self.lower()
		user_inputs = sentence.split(' ')
		war_count = 0
		ceb_count = 0
		hil_count = 0
		wars_count = 1
		cebs_count = 1
		hilis_count = 1

		for waray in warays:
			for user_input in user_inputs:
				if waray.word == user_input:
					war_count += (1 + 1) / (waray_count + doc_count)
					wars_count *= war_count
					wars_counts = wars_count / 2

		for cebu in cebus:
			for user_input in user_inputs:
				if cebu.word == user_input:
					ceb_count += (1 + 1) / (cebu_count + doc_count)
					cebs_count *= ceb_count
					cebs_counts = cebs_count / 2

		for hilig in hiligs:
			for user_input in user_inputs:
				if hilig.word == user_input:
					hil_count += (1 + 1) / (hili_count + doc_count)
					hilis_count *= hil_count
					hilis_counts = hilis_count / 2

		return wars_counts, cebs_counts, hilis_counts

	# def testing(self, user_input, waray_count, cebu_count, hili_count, doc_count, warays, hiligs, cebus):
	# 	war_count = 0
	# 	ceb_count = 0
	# 	hil_count = 0
	# 	smooth_war = 1
	# 	smooth_ceb = 1
	# 	smooth_hil = 1

	# 	priorLogWar = waray_count/doc_count
	# 	priorLogCeb = cebu_count/doc_count
	# 	priorLogHil = hili_count/doc_count


	# 	for waray in warays:
	# 		for user_input in user_inputs:
	# 			if waray.word != user_input:
	# 				war_count += 1 / (waray_count + doc_count)
	# 				wars_count *= war_count
	# 				smooth_war = wars_count / 2

	# 	for cebu in cebus:
	# 		for user_input in user_inputs:
	# 			if cebu.word != user_input:
	# 				ceb_count += 1 / (cebu_count + doc_count)
	# 				cebs_count *= ceb_count
	# 				smooth_ceb = cebs_count / 2

	# 	for hilig in hiligs:
	# 		for user_input in user_inputs:
	# 			if hilig.word != user_input:
	# 				hil_count += 1 / (hili_count + doc_count)
	# 				hilis_count *= hil_count
	# 				smooth_hil = hilis_count / 2

	# 	import pdb; pdb.set_trace()
	# 	return smooth_war, smooth_ceb, smooth_hil