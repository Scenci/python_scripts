#Python Tree Examples based on http://www.openbookproject.net/thinkcs/python/english2e/ch21.html
import sys

calls = 0

class Tree:
	def __init__(self, cargo, left=None, right=None):
		self.cargo = cargo
		self.left  = left
		self.right = right
    
	def __str__(self):
		return str(self.cargo)

def total(tree):
	global calls
	calls = calls + 1
	if tree == None:
		return 0
	return total(tree.left) + total(tree.right) + tree.cargo

def print_tree(tree):
	if tree == None:
		return
	print(tree.cargo)
	print_tree(tree.left)
	print_tree(tree.right)

def main():
	rec_var = 0
	#Tree(cargo, left, right) all generic.
	tree = Tree(3,Tree(9),Tree(6))
	tree.left.left = Tree(1)
	tree.right.right = Tree(12)
	
	#print out tree values recursively
	print_tree(tree)

	print('total = ', total(tree))
	print('No. of calls =',calls)

if __name__ == "__main__":
	main();	
