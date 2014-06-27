# depth first search --> check whether a graph is bipartite
# eliminate all mentions of colors --> get usual dfs
# we assume graph is connected, which can be checked via self.marked after a dfs

class dfsGraph():

	def __init__(self, n):
		self.size = n
		self.verts = [ i for i in range(0, self.size) ]
		self.edges = [ [] for i in self.verts]
		self.marked = [-1 for i in self.verts]
		self.edgeto = [-1 for i in self.verts]
		self.colors = [-1 for i in self.verts]
	
	def restore(self):  #keeps graph, allows for new search
		self.marked = [-1 for i in self.verts]
		self.edgeto = [-1 for i in self.verts]
		self.colors = [-1 for i in self.verts]

	def add_edge(self,a,b):
		(self.edges[a]).append(b)
		(self.edges[b]).append(a)
		
	def dfs(self, v):
		self.marked[v] = True
		
		if self.edgeto[v] == -1:
			self.edgeto[v] = v  #only set for initial vertex
			self.colors[v] = 0
			
		for w in self.edges[v]:
			if self.marked[w] == -1:
				self.marked[w] = True
				self.edgeto[w] = v
				self.colors[w] = (self.colors[v] + 1) % 2
				dfsGraph.dfs(self, w)		
			elif self.marked[w] == True:
				assert self.colors[w] == (self.colors[v] +1 ) %2
				#raises AssertionError if graph is not bipartite
				#otherwise print self.colors to see the bipartite vertex groupings
				
#example 1
g = dfsGraph(6)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(0,5)
g.add_edge(3,4)
g.add_edge(4,5)

print g.edgeto, g.marked
g.dfs(0)  #raises AssertionError


#example 2
h = dfsGraph(5)
h.add_edge(0,3)
h.add_edge(0,4)
h.add_edge(1,4)
h.add_edge(2,4)
h.dfs(4)
print h.colors



