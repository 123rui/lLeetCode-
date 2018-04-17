#全排列 深度优先搜索
def fullArrange(lis):
    global arrangeList
    arrangeList = []
    visits = [1 for i in range(len(lis))]
    oneList = []
    def dfs():
        #判断边界
        if sum(visits)==0:
            global arrangeList
            arrangeList.append(oneList.copy())   #注意这里的copy
            return
        #尝试没一种可能
        for i in range(len(lis)):
            if visits[i] == 1:
                oneList.append(lis[i])
                visits[i] = 0
                dfs()    #继续下一步
                oneList.pop()   #复原标记与路径
                visits[i] = 1
        return
    dfs()
    return arrangeList

lis = [4,2,6,17]
list_1 = fullArrange(lis)
print(list_1)
print(len(list_1))
