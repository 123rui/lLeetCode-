"""
leetcode 127 单词接龙
01  dfs  超时，通过19（共39）
02  dfs  修改添加边的方式，依然通过19

"""

def ladderLength( beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    #添加节点
    graph = {}
    for key in wordList:
        graph[key] = []
    if not beginWord in graph:
        graph[beginWord] = []


    def border(word1,word2):
        length = len(word1)
        if length == 0:
            return
        num = 0
        for i in range(length):
            if word1[i]==word2[i]:
                pass
            else:
                num += 1
            if num >= 2:
                return 0   #两个单词无法直接转换
        return 1

    #添加边
    # length = len(wordList)
    # for i in range(length):
    #     j = i + 1
    #     while j<length:
    #         if border(wordList[i],wordList[j]):
    #             graph[wordList[i]].append(wordList[j])
    #             graph[wordList[j]].append(wordList[i])
    #         j += 1

    #添加边2
    length = len(wordList)
    for key in graph:
        for i in range(length):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                new_word = key[0:i] + j +key[i+1:]
                if (new_word in graph)and new_word != key:
                    graph[key].append(new_word)


    def find_shortest_path(node_neighbors,start,end,path=[]):
        """
        寻找最短路径
        :param start: 开始节点
        :param end:  结束节点
        :param path:  路径
        :return: None
        """
        if start in path:
            return None
        path = path + [start]
        if start == end:
            return path
        if not start in node_neighbors.keys():
            return None
        shortest = None
        for node in node_neighbors[start]:
            newpath = find_shortest_path(node_neighbors,node,end,path)
            if newpath:
                if (not shortest) or len(newpath)<len(shortest):
                    shortest = newpath
        return shortest

    path = find_shortest_path(graph,beginWord,endWord)


    if path:
        return len(path)
    else :
        return 0


def ladderLength( beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    #添加节点
    graph = {}
    for key in wordList:
        graph[key] = []
    if not beginWord in graph:
        graph[beginWord] = []


    def border(word1,word2):
        length = len(word1)
        if length == 0:
            return
        num = 0
        for i in range(length):
            if word1[i]==word2[i]:
                pass
            else:
                num += 1
            if num >= 2:
                return 0   #两个单词无法直接转换
        return 1

    #添加边
    # length = len(wordList)
    # for i in range(length):
    #     j = i + 1
    #     while j<length:
    #         if border(wordList[i],wordList[j]):
    #             graph[wordList[i]].append(wordList[j])
    #             graph[wordList[j]].append(wordList[i])
    #         j += 1

    #添加边2
    length = len(wordList)
    for key in graph:
        for i in range(length):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                new_word = key[0:i] + j +key[i+1:]
                if (new_word in graph)and new_word != key:
                    graph[key].append(new_word)


    def find_shortest_path(node_neighbors,start,end):
        """
        寻找最短路径
        :param start: 开始节点
        :param end:  结束节点
        :param path:  路径
        :return: None
        """
        keys = [key for key in node_neighbors.key()]
        distance_dict = dict.fromkeys(keys,None)

        queue = []
        queue.append()

    path = find_shortest_path(graph,beginWord,endWord)


    if path:
        return len(path)
    else :
        return 0


lis = ["ted","tex","red","tax","tad","den","rex","pee"]
print(ladderLength("red","tax",lis))