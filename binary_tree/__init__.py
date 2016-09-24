class Node(object):
    '''节点类'''
    def ___init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    '''tree'''
    def __init__(self):
        self.root = Node()

    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node

        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:
                treeNode = myQueue.pop(0)
                if treeNode.lchild == None:
                    treeNode.lchild = node
                    return
                elif treeNode.rchild == None:
                    treeNode.rchild = node
                    return
                else:
                    myQueue.append(treeNode.lchild)
                    myQueue.append(treeNode.rchild)


    def front_digui(self, root):
        '''利用递归实现树的先序遍历'''

        if root == None:
            return
        print root.elem
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):

        if root == None:
            return
        self.middle_digui(root.lchild)
        print root.elem
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print root.elem

    def front_stack(self, root):
        '''利用堆栈实现树的先序遍历'''
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                print node.elem
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            node = node.rchild

    def middle_stack(self, root):
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.lchild
            node = myStack.pop()
            print node.elem
            node = node.rchild

    def later_stack(self, root):

        '''利用堆栈实现树的后序遍历'''

        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:
            node = myStack1.pop()
            if node.lchild:
                myStack1.append(node.lchild)
            if node.rchild:
                myStack1.append(node.rchild)
            myStack2.append(node)
        while myStack2:
            print myStack2.pop().elem

