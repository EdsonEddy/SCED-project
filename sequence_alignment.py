from math import ceil

class Sequence_alignment:
	def __init__(self, X, Y):
		self.X = X
		self.Y = Y
		self.cond_structs = {"if", "else", "elif"}
		self.iter_structs = {"for", "while"}

	def token_comparison(self, xi, yj):
		if xi[0] == yj[0]:
			return True
		elif xi[1] and yj[1] in self.cond_structs:
			return True
		elif xi[1] and yj[1] in self.iter_structs:
			return True	
		return False
		
	def levenshtein(self):
		X, Y = self.X, self.Y
		m = len(X) + 1
		n = len(Y) + 1
		t = [[0 for _ in range(n)] for _ in range(m)]
		for i in range(0, m):
			t[i][0] = i
		for i in range(1, n):
			t[0][i] = i
		for i in range(1, m):
			for j in range(1, n):
				cost = 0
				if not self.token_comparison(X[i - 1], Y[j - 1]):
					cost = 1
				t[i][j] = min(t[i - 1][j - 1] + cost, t[i][j - 1] + 1, t[i - 1][j] + 1)
		return t[m - 1][n - 1]

	def levenshtein_min_space(self):
		X, Y = self.X, self.Y
		if len(Y) > len(X):
			X, Y = Y, X
		m = len(X) + 1
		n = len(Y) + 1
		t = [[i for i in range(n)] for _ in range(2)]
		for i in range(1, m):
			t[0], t[1] = t[1], t[0]
			t[0][0] = i - 1
			t[1][0] = i 
			for j in range(1, n):
				cost = 0
				if not self.token_comparison(X[i - 1], Y[j - 1]):
					cost = 1
				t[1][j] = min(t[0][j - 1] + cost, t[1][j - 1] + 1, t[0][j] + 1)
		return t[1][n - 1]