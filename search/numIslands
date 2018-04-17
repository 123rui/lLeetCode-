"""
leetcode  200  岛屿的数量
01  dfs  172ms
02  bfs  164
"""

def numIslands( grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    if cols == 0:
        return 0

    num = 0

    next = [[0,1],[1,0],[-1,0],[0,-1]]
    visits = [[0 for i in range(cols)] for j in range(rows)]
    #visits = zeros.copy()
    def dfs(i,j):
        #判断边界
        if (i<0)|(rows<=i) or(j<0)|(cols<=j) :
            return
        if visits[i][j]==1 or grid[i][j]=='0':
            return
        visits[i][j] = 1
        for x,y in next:
            i += x
            j += y
            dfs(i,j)
            i -= x   #归位，很重要
            j -= y
        return

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]=='1' and visits[i][j]==0:
                dfs(i,j)
                num += 1
    return num

def numIslands2(grid):
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    if cols == 0:
        return 0

    num = 0

    next = [[0,1],[1,0],[-1,0],[0,-1]]
    visits = [[0 for i in range(cols)] for j in range(rows)]

    def bfs(i,j):
        if i<0 or rows<=i or j<0 or cols<=j:
            return
        if grid[i][j]=='0':
            return
        if visits[i][j]==1:
            return
        visits[i][j] = 1
        for x,y in next:
            i += x
            j += y
            bfs(i,j)
            i -= x
            j -= y
        return

    for i in range(rows):
        for j in range(cols):
            if visits[i][j]==0 and grid[i][j]=='1':
                bfs(i,j)
                num += 1
    return num



if __name__ == '__main__':
    #lis = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
    #print(numIslands(lis))
    lis = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(numIslands2(lis))
