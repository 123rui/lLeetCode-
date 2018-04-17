"""
leetcode 376 摇摆子序列
01  时间  48ms

"""
def wiggleMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    i = 0
    maxLength = 0
    if length>=1:
        maxLength +=1
    else :
        return 0
    if length>=2:
        if nums[i]<nums[i+1]:
            i += 1
            maxLength += 1
            sign = 1
        elif nums[i+1]<nums[i]:
            i += 1
            maxLength += 1
            sign = 0
        else:
            i += 1
            sign = -1

    while i<length-1:
        if sign==1:
            if nums[i+1]<nums[i]:
                i += 1
                maxLength += 1
                sign = 0
            else:
                i += 1
        elif sign==0:
            if nums[i]<nums[i+1]:
                i += 1
                maxLength += 1
                sign = 1
            else:
                i += 1
        else:
            if nums[i+1]<nums[i]:
                i += 1
                maxLength += 1
                sign = 0
            elif nums[i]<nums[i+1]:
                i += 1
                maxLength += 1
                sign = 1
            else :
                i += 1


    return maxLength

if __name__ == '__main__':
    lis = [1,7,4,9,2,5]
    print(wiggleMaxLength(lis))
