from graph import Graph
import time


g = Graph()
alt =  [['A','C','D','H','E'],['F','B','G','M','I'],['J','K','L','R','N'],['O','P','Q','S','X'],['T','U','V','W',0]]
goal = [['A','B','C','D','E'],['F','G',0,'H','I'],['J','K','L','M','N'],['O','P','Q','R','S'],['T','U','V','W','X']]

g.setMatrix(goal)

print("Graph:")
g.printGraph()

print("Path Build\n")


bt0 = time.clock()
bsf = g.bfs(alt, goal)
bt1 = time.clock()

print("matrix")
for a in alt:
	print(a)

print("BreadthFirst:", bsf.getDir(), "time:", bt1 - bt0)

