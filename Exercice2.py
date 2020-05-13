from Exercice1 import *
class BinaryTree:
    def __init__(self,root):
        self.__root = root
    def getRoot(self):
        return self.__root

    def isRoot(self,Node):
        if Node == self.__root:
            return True
        else: return False

    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.getLeft()) + 1 + self.size(node.getRight())

    def sumValues(self,node):
        if node is None:
            return 0
        else:
            return self.sumValues(node.getLeft()) + node.getVal() + self.sumValues(node.getRight())

    def numberLeaves(self, node):
         if node is None:
             return 0
         else:
             if node.getLeft() and node.getRight() is None:
                print("True")
             else:
                return self.numberLeaves(node.getLeft() + node.getRight())

arbre = BinaryTree(Node(12,None,None))
arbre.getRoot().setLeft(Node(5,None,None))
arbre.getRoot().getLeft().setLeft(Node(4,None,None))
arbre.getRoot().getLeft().setRight(Node(6,None,None))
arbre.getRoot().getLeft().getLeft().setLeft(Node(3,None,None))

arbre.getRoot().setRight(Node(17,None,None))
arbre.getRoot().getRight().setRight(Node(19,None,None))
arbre.getRoot().getRight().getRight().setLeft(Node(18,None,None))
arbre.getRoot().getRight().getRight().setRight(Node(21,None,None))

print(arbre.size(arbre.getRoot()))
print(arbre.sumValues(arbre.getRoot()))
print(arbre.numberLeaves(arbre.getRoot()))
