from path import Path

class BreadthFirst:
	def __init__(self, ver = {}):
		self.expl = []
		self.correctState  = [[]]
		self.bufferState = [[]]
		self.nodes = ver


	def run(self, buff, goal):
		self.bufferState = buff
		self.correctState = goal
		self.expl = []
		pa = Path(self.findZero())
		sa = {pa: self.generate(pa)}
		return self.gotoF(sa)


	def gotoF(self, arr, sen = 0):
		sen += 1
		va, pa = self.BfsIter(arr)

		
		if sen == 80:
			print("Forded Quit")
			quit()

		if pa == None:
			return self.gotoF(va, sen)

		else:
			return va, pa


	def BfsIter(self, arr):
		sav = None
		g = {}

		if arr == None:
			return arr, sav

		for k, a in arr.items():
			if a == None:
				continue
			if type(a) == type({}):
				v, res = self.BfsIter(a)
				if res != None:
					sav = res
					return arr, sav
			else:
				info = self.inList(a)
				if info != None:
					return arr, info
				else:
					arr[k] = self.expand(a)


		return arr, sav


	def inList(self, arr):
		for a in arr:
			if self.checkState(a):
				return a

		return None


	def expand(self, keys):
		val = {}
		for a in keys:
			if self.checkState(a, 1):
				val[a] = None
			else:
				val[a] = self.generate(a)
		return val


	def generate(self, key):
		n = []
		for a in list(self.nodes[key.getName()].getConnections()):
			n.append(self.getNeighbors(a, key))


		return n


	def getNeighbors(self, ver, key):
		com = key.getDir() + [self.nodes[key.getName()].getDirection(ver)]
		if type(ver) != type(1) and type(ver) != type(chr(70)):
			return Path(ver.getId(), key.getPath(), com)
		else:
			return Path(ver, key.getPath(), com)


		return n

	def setNodes(self, nod):
		self.nodes = nod


	def addNode(self, key, nod):
		self.nodes[key] = nod

	def findZero(self):
		for a in range(len(self.correctState)):
			for b in range(len(self.correctState[a])):
				if self.bufferState[a][b] == 0:
					return self.correctState[a][b]
		return 0

	def findPlace(self, ex):
		for a in range(len(self.correctState)):
			for b in range(len(self.correctState[a])):
				if self.correctState[a][b] == ex:
					return a, b
		return 0

	def checkState(self, pat, et = None):
		#print("pat:", pat.getPath())
		ex = [[x for x in y] for y in self.bufferState]
		ru = [x for x in pat.getPath()]
		pa = ru.pop(0)


		for a in ru:
			g, m = self.findPlace(pa)
			q, w = self.findPlace(a)

			cVa = ex[g][m]
			aVa = ex[q][w]

			ex[g][m] = aVa
			ex[q][w] = cVa
			pa = a

		if et == None:
			if ex == self.correctState:
				return True

		else:
			if ex in self.expl:
				return True
			else:
				self.expl.append(ex)


		return False


