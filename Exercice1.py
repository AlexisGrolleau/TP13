
class Node:
    def __init__(self,val,left,right):
        self.__val = val
        self.__right = right
        self.__left = left
    def getVal(self):
        return self.__val
    def getRight(self):
        return self.__right
    def getLeft(self):
        return self.__left
    def setRight(self,node):
        self.__right = node
    def setLeft(self,node):
        self.__left = node
    def __str__(self):
        return str(self.__val)

node1 = Node(3,None,None)

"""node2 = Node(4,None,None)
node3 = Node(1,node1,node2)
print(node3.getLeft().getVal())
"""""
