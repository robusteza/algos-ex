class MH(object):  #min heap

	def __init__(self, f = (lambda x: x) ):  #default comparison function is id
		self.list = []
		self.compare = f
	
	def children(self,i):
		if len(self.list) <= 2*i +1:
			return None
		elif len(self.list) == 2*i + 2:
			return [self.list[2*i +1]]
		else:
			return [self.list[2*i + 1], self.list[2*i +  2]]
	
	def parent(self,i):
		if i % 2 == 0:
			return self.list[ (i - 2) / 2]
		else: return self.list[ (i - 1) / 2]
		
	def parent_index(self, i):
		if i % 2 == 0:
			return (i - 2) / 2
		else: return (i - 1) / 2

	def values(self, list1):
		if list1 == None:
			return None
		else:
			return [ self.compare(item) for item in list1]
	
	def sink(self, j): #move down self.list[j] appropriately; finds correct loc if j=0
	 	if  MH.children(self,j) != None:
			while min(MH.values(self, MH.children(self,j))) < self.compare(self.list[j]):
				y = min(MH.values(self, MH.children(self,j)))
				x = MH.values(self, MH.children(self,j)).index(y) #0 or 1
				z = self.list[j]
				self.list[j] = self.list[2*j + 1 + x]
				self.list[2*j + 1 + x] = z
				j = 2*j +1 +x
				if  MH.children(self,j) == None: break
	
	def swim(self,j): #move up self.list[j] appropriately; finds correct loc if j = -1
		while j > 0 and self.compare(MH.parent(self,j)) > self.compare(self.list[j]):
			z = self.list[j]
			self.list[j] = self.list[MH.parent_index(self, j)]
			self.list[MH.parent_index(self, j)] = z
			j = MH.parent_index(self, j)
	
	def insert(self, x):
		self.list.append(x)
		MH.swim(self,len(self.list)-1)
		
	def pop(self):
		if len(self.list) == 0:
			return 'empty list'
		else:
			y = self.list[0]
			self.list[0] = self.list[-1]
			self.list  = self.list[0:len(self.list)-1]
			MH.sink(self,0) #restore the heap
			return y
			
			
class SP(object): #shortest path

	def __init__(self, n):
		self.size = n #number of vertices
		self.verts = [i for i in range(0,self.size)]
		self.edges = [[] for vert in self.verts]
		self.source = self.verts[0]
		self.target = self.verts[self.size-1]
		self.marked = [False for i in self.verts]
		self.dist = [float('inf') for i in self.verts] 
		self.dist[0] = 0
		self.edgeto = [-1 for i in self.verts]
		self.edgeto[0] = 0
		self.PQ = MH(lambda (x,y) : y)
		
	def ins_edge(self, a,b,w): #edge from a to b with weight w
		self.edges[a].append((b,w))
		
	def relax(self,a):
		for (b,w) in self.edges[a]:
			if self.marked[b] == False:
				if self.dist[b] == float('inf'):  #first time b enters the heap
					self.dist[b] = self.dist[a] + w
					self.edgeto[b] = (a,b)
					self.PQ.insert((b,self.dist[b]))
				elif self.dist[a] + w < self.dist[b]: #b already on heap, but found better path
					c = self.dist[b]
					self.dist[b] = self.dist[a] + w
					self.edgeto[b] = (a,b)
					a = self.PQ.list.index((b,c)) #the index of the old pair
					self.PQ.list[a] = (b,self.dist[b]) #replace with new distance
					self.PQ.swim(a) #distance decreased, so can only swim up
					
	def SPS(self):
		self.PQ.insert((0,0))
		while self.marked != [True for i in self.verts]:
			x = self.PQ.pop()
			if self.marked[x[0]] == True: break
			else:
				self.marked[x[0]] = True
				SP.relax(self,x[0])



#a copied example


A = SP(8)

A.ins_edge(4,5,0.35)
A.ins_edge(5,4,0.35)
A.ins_edge(4,6,0.37)
A.ins_edge(5,6,0.28)
A.ins_edge(6,5,0.28)
A.ins_edge(5,1,0.32)
A.ins_edge(0,4,0.38)
A.ins_edge(0,2,0.26)
A.ins_edge(6,3,0.39)
A.ins_edge(1,3,0.29)
A.ins_edge(2,6,0.34)
A.ins_edge(7,2,0.40)
A.ins_edge(3,7,0.52)
A.ins_edge(7,0,0.58)
A.ins_edge(7,4,0.93)

print A.edgeto

print A.dist, 'dist'

A.SPS()

print A.edgeto

print A.dist
