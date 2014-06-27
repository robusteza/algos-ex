#calculate how many sites in a 20x20 grid must be open for the system to percolate, i.e.,
#for an open site in the top row to be connected (via open sites) to an open site in the bottom row
#exercise from Princeton/Coursera algorithms course

import math
import random
import numpy

def trial():

	SitesList = ['A','B']
	OpenSitesList = ['A','B']
	N = 20 #gridsize
	
 	for i in range(1,N+1):
 	  for j in range(1,N+1):
 		SitesList.append((i,j))
	
	ParentDict = {}
	SizeDict = {}  #will keep track of tree size as we open sites
	for x in SitesList:
		ParentDict[x] = -1
		SizeDict[x] = -1  #everybody closed
	
	#'A' (resp. 'B') is a neighbor of everybody in the top (resp. bottom) row
	ParentDict['A'] = 'A'
	ParentDict['B'] = 'B'
	SizeDict['A'] = 1  #starts out as open
	SizeDict['B'] = 1  #starts out as open
	
	def Neighbors(x):
	#returns list of (up to 4) neighbors of a site in the grid
	  l = []
	  if x[0] != 1:
		l.append((x[0]-1,x[1]))
	  if x[0] == 1:
		l.append('A')
	  if x[0] != N:
		l.append((x[0]+1,x[1]))
	  if x[0] == N:
		l.append('B')
	  if x[1] != 1:
		l.append((x[0],x[1]-1))
	  if x[1] != N:
		l.append((x[0],x[1]+1))
	  return l

	def root(x):
	  if ParentDict[x] == -1:
		return -1
	  else:
		while ParentDict[x] != x:
		  x = ParentDict[x]
		return x
	
	def Update(x):
	  OpenNeighbors = []
	  OpenSizes = []

	  for y in Neighbors(x):
		if SizeDict[y] >= 0:
		  OpenNeighbors.append(y)  #make list of neighbors of x who are eopen
		  OpenSizes.append(SizeDict[y]) #sizes of the trees to which neighbors belong

	  assert len(OpenNeighbors) == len(OpenSizes)  

	  if OpenNeighbors == []:   
		SizeDict[x] = 1
		ParentDict[x] = x
	  if len(OpenNeighbors) == 1:
		ParentDict[x] = root(OpenNeighbors[0])
		SizeDict[root(OpenNeighbors[0])] += 1
	  if len(OpenNeighbors) >= 2:  #in this case, attach x to the smaller tree
		a = numpy.argmin(OpenSizes)
		ParentDict[x] = root(OpenNeighbors[a])
		b = numpy.argmax(OpenSizes)
		for i in range(0,len(OpenSizes)):
		  ParentDict[root(OpenNeighbors[i])] = root(OpenNeighbors[b])

	  for x in SizeDict.keys():
		if root(x) != -1:
		  SizeDict[x] = SizeDict[root(x)]
		
	def IsConnected(x,y):
	  if root(x) == root(y) and root(x) != -1:
		return True
	  else: return False

	i = 0
	while IsConnected('A','B') == False:
		a = random.randint(1,N)
		b = random.randint(1,N)
		if (a,b) not in OpenSitesList:
			i +=1
      		OpenSitesList.append((a,b))
      		Update((a,b))
		continue
  	return i


#experiment
list = []

while len(list) < 100:
   list.append(trial())

print list
list = numpy.array(list)
print numpy.mean(list)
print numpy.std(list)
