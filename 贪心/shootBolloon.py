"""
leetcode  452  引爆气球
01  贪心  196ms

"""
def findMinArrowShots( points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    #根据x_start排序
    points.sort()

    i = 0
    j = 0
    num = 0
    length = len(points)

    while j < length :
        while points[i][1] >= points[j][0]  :
            points[i][1] = min(points[i][1],points[j][1])
            j += 1
            if j >= length:
                break
        i = j
        num += 1
    return num

if __name__ == '__main__':
    lis = [[10,16],[2,8],[1,6],[7,21]]
    print(findMinArrowShots(lis))
    lis = [[10,16],[2,8],[1,6]]
    print(findMinArrowShots(lis))