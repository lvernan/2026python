"""
二叉树数据结构的练习
"""
class Node(): #结点的数据结构
    def __init__(self,element = -1,lchild = None,rchild = None):
        self.element = element
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree(): #二叉树的数据结构
    def __init__(self): #初始化二叉树
        self.root = None
        self.arr = []

    def Add_Node(self,node:Node): #给二叉树添加结点
        if self.root is None:
            self.root = node
            self.arr.append(node)
        else:
            self.arr.append(node)
            if self.arr[0].lchild is None:
                self.arr[0].lchild = node #放入右孩子
            else:
                self.arr[0].rchild = node #放入左孩子
                self.arr.pop(0)

    def Pre_Order(self,current_node:Node): #先序遍历
        if current_node is not None:
            print(current_node.element,end=' ')
            self.Pre_Order(current_node.lchild)
            self.Pre_Order(current_node.rchild)

    def In_Order(self,current_node:Node): #中序遍历
        if current_node is not None:
            self.In_Order(current_node.lchild)
            print(current_node.element, end=' ')
            self.In_Order(current_node.rchild)

    def Post_Order(self,current_node:Node): #后序遍历
        if current_node is not None:
            self.Post_Order(current_node.lchild)
            self.Post_Order(current_node.rchild)
            print(current_node.element, end=' ')

    def Cen_Order(self): #层序遍历
        help_arr = [] #创建辅助队列
        help_arr.append(self.root) #让根结点入队
        while help_arr:
            out_node:Node = help_arr.pop(0)
            print(out_node.element,end=' ')
            if out_node.lchild is not None:
                help_arr.append(out_node.lchild)
            if out_node.rchild is not None:
                help_arr.append(out_node.rchild)

if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1,11):
        new_node = Node(i)
        tree.Add_Node(new_node)
    tree.Pre_Order(tree.root)
    print()
    tree.In_Order(tree.root)
    print()
    tree.Post_Order(tree.root)
    print()
    tree.Cen_Order()
    print()