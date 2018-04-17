"""
leetcode 455分发饼干
01 并归排序 484ms
02 堆排序   116ms
03 自带sort函数  112ms
"""
def findContentChildren(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """

    ###二路归并
    # 输入：列表   输出：列表
    # 函数作用：
    # 将list_1中索引为start—mid和mid+1—end两个子序列二路归并，其他部分不改变
    # 归并后list_1
    def merge(list_1, start, mid, end):
        list_A = list_1[start:mid + 1]  # 开辟A段缓存,长度为mid+1-start
        length = mid + 1 - start
        i = start  # 指向合并列表
        j = 0  # 指向A列表
        g = mid + 1  # 指向B列表
        while (j < length) & (g <= end):
            if list_1[g] < list_A[j]:  # B列表靠后，相等时先插入A中元素
                list_1[i] = list_1[g]
                i += 1
                g += 1
            else:
                list_1[i] = list_A[j]
                i += 1
                j += 1
        if g == end + 1:  # B列表先放完
            list_1[i:end + 1] = list_A[j:mid + 1]
        return list_1[start:end + 1]

    ###归并排序
    def mergeSort(list_1, start, end):
        if end - start <= 2:
            if list_1[start + 1] > list_1[end]:  # 保证传入都为有序序列
                list_1[start + 1], list_1[end] = list_1[end], list_1[start + 1]
            return merge(list_1, start, start, end)
        mid = (start + end) // 2
        list_1[start:mid + 1] = mergeSort(list_1[start:end + 1], start - start, mid - start)
        list_1[mid + 1:end + 1] = mergeSort(list_1[start:end + 1], mid + 1 - start, end - start)
        return merge(list_1, start, mid, end)

    ###归并排序
    #g = mergeSort(g,0,len(g)-1)
    #s = mergeSort(s,0,len(s)-1)

    ###堆排序
    import heapq

    def heapqSort(lis):
        heapq.heapify(lis)
        return  [heapq.heappop(lis) for i in range(len(lis))]

    g = heapqSort(g)
    s = heapqSort(s)

    i = 0
    j = 0

    length_i = len(g)
    length_j = len(s)

    num = 0

    while i<length_i:
        while j<length_j:
            if g[i]<=s[j]:
              num += 1
              j += 1
              break
            j += 1
        i += 1
    print(num)
    return

g = [1,2,3,6,9]
s = [1,1,4,8]

findContentChildren(g,s)