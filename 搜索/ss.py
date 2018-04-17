"""
创建2018.4.12  杨锐
"""
import copy


class Node:
    def __init__(self, data):
        self.data = data
        self.Rchild = None
        self.Lchild = None
        self.child_number = 0
        self.parent = None

    def set_parent(self, node):
        """
        设置父节点
        """
        self.parent = node

    def add_Rchild(self, this_node):
        """
        添加右孩子
        param ：this_node :所添加的子节点node 型或value
        return None
        """
        # 判断是否为node型
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(None, this_node)
        # 添加
        if self.Rchild is not None:
            self.Rchild = this_node
        else:
            self.Rchild = this_node
            self.child_number += 1
        this_node.set_parent(self)

    def drop_Rchild(self):
        """
        删除右孩子
        """
        self.Rchild = None
        self.child_number -= 1

    def add_Lchild(self, this_node):
        """
        添加左孩子
        param ：this_node :所添加的子节点node 型或value
        return None
        """
        # 判断是否为node型
        if isinstance(this_node, Node):
            pass
        else:
            this_node = Node(None, this_node)
        if self.Lchild is not None:
            self.Lchild = this_node
        else:
            self.Lchild = this_node
            self.child_number += 1
        this_node.set_parent(self)

    def drop_Lchild(self):
        self.Lchild = None
        self.child_number -= 1


class Tree:

    def __init__(self):
        """
        根节点
        """
        self.root = None
        return

    def add(self, item):
        """
        添加节点，利用队列，其添加方式与层次遍历的搜索顺序一样
        param item：添加的节点的数据值 value
        return None
        """
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.Lchild is None:
                    pop_node.Lchild = node
                    return
                elif pop_node.Rchild is None:
                    pop_node.Rchild = node
                    return
                else:
                    q.append(pop_node.Lchild)
                    q.append(pop_node.Rchild)
        return

    def batchAdd(self, lis):
        """
        批量加入节点
        param lis:列表，包含需要批量加入的数据
        return ：None
        """
        length = len(lis)
        if self.root is None:
            self.root = Node(lis.pop(0))
            length -= 1
        queue = [self.root]
        while length:
            node = queue.pop(0)
            if node.Lchild is None:
                node.Lchild = Node(lis.pop(0))
                length -= 1
            if (node.Rchild == None) & (length != 0):
                node.Rchild = Node(lis.pop(0))
                length -= 1
            queue.append(node.Lchild)
            if node.Rchild is not None:
                queue.append(node.Rchild)
        return

    def preOrder(self):
        """
        先序遍历，利用list的pop和append函数构建一个栈
        return: list  包含先序遍历的所有数据
        """
        if not self.root:
            return []
        preList = []
        stackNode = []
        stackNode.append(self.root)
        while stackNode:
            node = stackNode.pop()
            preList.append(node.data)
            if node.Rchild:
                stackNode.append(node.Rchild)
            if node.Lchild:
                stackNode.append(node.Lchild)
        return preList

    def midOrder(self):
        """
        中序遍历
        return ：list  包含中序遍历的所有数据
        """
        if not self.root:
            return []
        midList = []
        stackNode = []
        node = self.root
        while stackNode or node:
            while node:
                stackNode.append(node)
                node = node.Lchild
            node = stackNode.pop()
            midList.append(node.data)
            node = node.Rchild
        return midList

    def aftOrder(self):
        """
        后序遍历
        return : list  包含后序遍历的所有数据
        """
        if self.root is None:
            return []
        aftList = []
        stack1Node = []
        stack2Node = []
        node = self.root
        stack1Node.append(node)
        while stack1Node:  # 通过这个循环获得一个后序遍历的逆序存放于stack2中（即根节点-右子树-左子树）
            node = stack1Node.pop()
            if node.Lchild:
                stack1Node.append(node.Lchild)
            if node.Rchild:
                stack1Node.append(node.Rchild)
            stack2Node.append(node)
        while stack2Node:  # 将stack2中的数据出栈给list
            node = stack2Node.pop()
            aftList.append(node.data)
        return aftList

    def levelOrder(self):
        """
        层次遍历，利用一个队列
        return:list  包含层次遍历的所有数据
        """
        if self.root is None:
            return []
        levelList = []
        queue = []
        node = self.root
        queue.append(node)
        while queue:
            node = queue.pop(0)
            if node.Lchild is not None:
                queue.append(node.Lchild)
            if node.Rchild is not None:
                queue.append(node.Rchild)
            levelList.append(node.data)
        return levelList


class Graph:
    def __init__(self, maps=[], nodenum=0, edgenum=0):
        self.map = maps  # 图的矩阵结构
        self.nodenum = len(maps)
        self.edgenum = edgenum

    #   self.nodenum = GetNodenum()#节点数
    #  self.edgenum = GetEdgenum()#边数
    def isOutRange(self, x):
        try:
            if x >= self.nodenum or x <= 0:
                raise IndexError
        except IndexError:
            print("节点下标出界")

    def GetNodenum(self):
        self.nodenum = len(self.map)
        return self.nodenum

    def GetEdgenum(self):
        GetNodenum()
        self.edgenum = 0
        for i in range(self.nodenum):
            for j in range(self.nodenum):
                if self.map[i][j] is 1:
                    self.edgenum = self.edgenum + 1
        return self.edgenum

    def InsertNode(self):
        for i in range(self.nodenum):
            self.map[i].append(0)
        self.nodenum = self.nodenum + 1
        ls = [0] * self.nodenum
        self.map.append(ls)

    # 假删除，只是归零而已
    def DeleteNode(self, x):
        for i in range(self.nodenum):
            if self.map[i][x] is 1:
                self.map[i][x] = 0
                self.edgenum = self.edgenum - 1
            if self.map[x][i] is 1:
                self.map[x][i] = 0
                self.edgenum = self.edgenum - 1

    def AddEdge(self, x, y):
        if self.map[x][y] is 0:
            self.map[x][y] = 1
            self.edgenum = self.edgenum + 1

    def RemoveEdge(self, x, y):
        if self.map[x][y] is 0:
            self.map[x][y] = 1
            self.edgenum = self.edgenum + 1

    def BreadthFirstSearch(self):
        def BFS(self, i):
            print(i)
            visited[i] = 1
            for k in range(self.nodenum):
                if self.map[i][k] == 1 and visited[k] == 0:
                    BFS(self, k)

        visited = [0] * self.nodenum
        for i in range(self.nodenum):
            if visited[i] is 0:
                BFS(self, i)

    def DepthFirstSearch(self):
        def DFS(self, i, queue):

            queue.append(i)
            print(i)
            visited[i] = 1
            if len(queue) != 0:
                w = queue.pop()
                for k in range(self.nodenum):
                    if self.map[w][k] is 1 and visited[k] is 0:
                        DFS(self, k, queue)

        visited = [0] * self.nodenum
        queue = []
        for i in range(self.nodenum):
            if visited[i] is 0:
                DFS(self, i, queue)