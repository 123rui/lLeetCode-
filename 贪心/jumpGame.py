"""
leetcode  55  跳跃游戏
01   贪心   88ms

"""

def canJump( nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    new = 0
    new_max = 0
    next_max = nums[0]

    length = len(nums)

    while (new_max < next_max)&(next_max < length):
        new_max = next_max
        #找到下一个next_max
        while new <= new_max:
            if next_max < (new + nums[new]):
                next_max = new + nums[new]
            new += 1

    if next_max >= length - 1:
        return True
    else:
        return False


if __name__ == '__main__':
    lis = [2,3,1,1,4]
    print(canJump(lis))
    lis = [3,2,1,0,4]
    print(canJump(lis))