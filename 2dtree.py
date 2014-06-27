#treesort and a 2dtree

class Tree(object):

	def __init__(self): #, left, right):
		self.root = None  #need to handle no arguments
		self.leftsub = None
		self.rightsub = None

	def insert(self,p):
		if self.root == None:
			self.root = p
			self.leftsub = Tree()
			self.rightsub = Tree()
		elif p <= self.root:
			Tree.insert(self.leftsub,p)
		elif p > self.root:
			Tree.insert(self.rightsub,p)

	def print_tree(self):
		if self.root == None:
			return ''
		else:
			return Tree.print_tree(self.leftsub) + str(self.root) + ',' + Tree.print_tree(self.rightsub)

#example
T = Tree()
T.insert(4)
T.insert(6)
T.insert(1)
T.insert(10)
T.insert(7)
T.insert(3)
T.insert(11)
T.insert(8)
T.insert(5)
T.insert(9)

print Tree.print_tree(T)



class Point():

	def __init__(self,x,y):
		self.x = x
		self.y = y


class kdTree():
	#k=2
	def __init__(self, a): #, left, right):
		self.dim = a
		self.root = None
		self.leftsub = None
		self.rightsub = None

	def insert(self,p):
		if self.root == None:
			self.root = p
			if self.dim == 'x':
				self.leftsub = kdTree('y')
				self.rightsub = kdTree('y')
			elif self.dim == 'y':
				self.leftsub = kdTree('x')
				self.rightsub = kdTree('x')
		elif self.dim == 'x':
			if p.x <= self.root.x:
				kdTree.insert(self.leftsub,p)
			elif p.x > self.root.x:
				kdTree.insert(self.rightsub,p)
		elif self.dim == 'y':
			if p.y <= self.root.y:
				kdTree.insert(self.leftsub,p)
			elif p.x > self.root.y:
				kdTree.insert(self.rightsub,p)
				
	def print_tree(self):
		if self.root == None:
			return ''
		else:
			return [kdTree.print_tree(self.leftsub), (self.root.x, self.root.y), kdTree.print_tree(self.rightsub)]


#example
p = Point(3,4)
q = Point(1,5)
r = Point(2,2)
s = Point(9,1)
m = Point(4,7)
t = kdTree('x')


t.insert(p)
t.insert(q)
t.insert(r)
t.insert(s)
t.insert(m)

print kdTree.print_tree(t)

