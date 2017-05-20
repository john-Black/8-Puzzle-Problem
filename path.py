#This class creates the path
class Path:
	def __init__(self, name, br = [], di = [], mat = []):
		self.node = name
		self.tree = br + [name]
		self.matrix = mat
		self.moves = di


	def addPathVertex(self, nod):
		self.tree.append(nod)


	def getPath(self):
		return self.tree


	def __str__(self):
		return str(self.node)

	def __repr__(self):
		return str(self.node)

	def getName(self):
		return self.node

	def setPath(self, aw):
		self.tree = aw


	def setMatrix(self, mat):
		self.matrix = mat

	def getMatrix(self):
		return self.matrix

	def setDir(self, di):
		self.moves = di

	def getDir(self):
		return self.moves

	def addDir(self, di):
		self.moves.append(di)
