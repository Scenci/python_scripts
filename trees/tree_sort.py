#Python Tree Examples based on http://www.openbookproject.net/thinkcs/python/english2e/ch21.html
import sys
import time
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

def tree_traverse(root):
    time.sleep(.75)
    print(root)
    if(root == None):
        return
    if(tree_traverse(root.left) == None and tree_traverse(root.right) == None):
        #Work here
        print('reached')
        return

def print_tree(tree):
	if tree == None:
		return
	print(tree.cargo)
	print_tree(tree.left)
	print_tree(tree.right)

def main():
	
        #Tree(cargo, left, right) all generic.
	
        #Build a Tree
        root = Tree(6,Tree(4),Tree(5))
        
        #Traverse Tree
        tree_traverse(root)

        #print out tree values recursively
        #print_tree(root)

        #print('total = ', total(root))
        #print('No. of calls =',calls)

if __name__ == "__main__":
	main();	
