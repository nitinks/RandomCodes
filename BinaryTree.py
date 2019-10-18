#!/usr/bin/python

class Node:
	rchild,lchild,data = None,None,None

	def __init__(self,key):
		self.rchild = None
		self.lchild = None
		self.data = key
class Tree:
	lst = []
	def __init__(self):
		self.root = None

	def insert(self,node,somenumber):
		
		if self.root is None:
			self.root = Node(somenumber)
		#	print node.data
		else:
			if node.data < somenumber:
				if node.rchild == None:
					node.rchild = Node(somenumber)
				else:
					self.insert(node.rchild, somenumber)
			elif node.data > somenumber:
				if node.lchild == None:
					node.lchild = Node(somenumber)
				else:
					self.insert(node.lchild,somenumber)
			else:
				print "same data!can't insert"

	def inorder(self,node):
		if node.lchild:
			self.inorder(node.lchild)
		print node.data
		self.lst.append(node.data)
		if node.rchild:
			self.inorder(node.rchild)
		return self.lst

	def finddistance(self,lst,firstnode,secnode):
		fcount = 0
		scount = 0
		firstposition = 0
		secposition = 0
		for i in lst:
			fcount = fcount + 1
			if i == firstnode:
				firstposition = fcount
		for j in lst:
			scount = scount + 1
			if j == secnode:
				secposition = scount	
		if secposition > firstposition:
			distance = secposition - firstposition
		else:
			distance = firstposition - secposition
		print "distance between two nodes:"
		print distance			
		
	
t = Tree()
t.insert(t.root,4)


t.insert(t.root,5)
t.insert(t.root,3)
t.insert(t.root,6)
t.insert(t.root,4)

lst = t.inorder(t.root)
t.finddistance(lst,4,6)
