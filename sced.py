from lexer import Lexer
from sequence_alignment import Sequence_alignment
from ufds import UFDS

import os
import shutil

class SCED:

	def __init__(self, *args):
		# two args string and integer: path_directory and percentage
		if isinstance(args[0], str) and isinstance(args[1], int):
			self.file_paths = args[0]
			self.percentage = args[1]
			self.arr_file_path = []
			self.arr_file_tokens = []
			for file in os.listdir(self.file_paths):
				file_path = os.path.join(self.file_paths, file)
				if os.path.isfile(file_path):
					lexical_analizer = Lexer(file_path)
					self.arr_file_tokens.append(lexical_analizer.tokens)
					self.arr_file_path.append(file_path)
		# two args strings: file_path, file_path
		else:
			self.file_path_a = args[0]
			self.file_path_b = args[1]

	def group_mode(self):
		set_disjoint = UFDS(len(self.arr_file_tokens))
		for i in range(len(self.arr_file_path) - 1):
			for j in range(i + 1, len(self.arr_file_path)):
				if not set_disjoint.in_same_set(i, j):
					if self.get_percentage(self.arr_file_tokens[i], self.arr_file_tokens[j]) >= self.percentage:
						set_disjoint.union(i, j)
		sim_detect = []
		for idx, i in enumerate(set_disjoint.parents):
			if set_disjoint.size(i) == 1:
				continue
			elif idx != i:
				file_a = self.arr_file_path[i].split("\\")[-1]
				file_b = self.arr_file_path[idx].split("\\")[-1]
				sim_detect.append([file_a, file_b])
		return sim_detect

	def allpair_mode(self):
		sim_detect = []
		for i in range(len(self.arr_file_path) - 1):
			for j in range(i + 1, len(self.arr_file_path)):
				per = self.get_percentage(self.arr_file_tokens[i], self.arr_file_tokens[j])
				if per >= self.percentage:
					file_a = self.arr_file_path[i].split("\\")[-1]
					file_b = self.arr_file_path[j].split("\\")[-1]
					sim_detect.append([file_a, file_b, per])
		return sim_detect

	def pair_mode(self):
		arr_tokens_a = Lexer(self.file_path_a).tokens
		arr_tokens_b = Lexer(self.file_path_b).tokens
		per = self.get_percentage(arr_tokens_a, arr_tokens_b)
		return [self.file_path_a, self.file_path_b, per]

	def get_percentage(self, arr_tokens_a, arr_tokens_b):
		seq_align = Sequence_alignment(arr_tokens_a, arr_tokens_b)
		edit_distance = seq_align.levenshtein_min_space()
		max_len = max(len(arr_tokens_a), len(arr_tokens_b))
		percentage = (1 - edit_distance / max_len) * 100
		return round(percentage, 2)
