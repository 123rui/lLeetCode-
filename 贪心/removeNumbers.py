"""
leetcode  402 移除k位数字
01  时间  72ms

"""

def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    #num是否为空
    if num :
        i = 0
        length = len(num)
        stack = []
        stack.append(num[i])
        i += 1
        while (k>0)&(i<length):
          if stack:    #stack不为空
            if stack[-1]>num[i]:
                stack.pop()
                k -= 1
            else:
                stack.append(num[i])
                i += 1
          else:
              stack.append(num[i])
              i += 1
        if k == 0 :
            while i<length:
                stack.append(num[i])
                i += 1
        else:
            while k!=0 and stack:
                stack.pop()
                k -= 1
        # 去除字符串前面的0
        while stack and stack[0] == "0":  #注意这里是字符串0
            stack.pop(0)
        num = ''.join(stack)
        if len(num)==0:
            num = "0"
        return num
    else:
        return ""


if __name__ == "__main__":
    #num = "1432219"
    #k = 3
    #num = "112"
    #k = 1
    num = "10200"
    k = 1
    print(removeKdigits(num,k))