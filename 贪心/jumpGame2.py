"""
leetcode  45  跳跃游戏2
01  时间  76ms

"""
def jump( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    new = 0
    #new_max = 0
    next_max = nums[0]
    step = 0

    length = len(nums)
    if length == 1:
        return step
    step += 1
    while next_max < length -1 :
        new_max = next_max
        while new <= new_max:
            if next_max < (new + nums[new]):
                next_max = new + nums[new]
            new += 1
        step += 1
    return step

if __name__ == '__main__':
    lis = [2,3,1,1,4]
    print(jump(lis))