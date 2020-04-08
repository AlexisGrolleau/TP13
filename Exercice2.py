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

    def size(self,Node):
        if Node.getLeft() == None:
            return 1
        else:
            return arbre.size(Node.getLeft()) +1



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
