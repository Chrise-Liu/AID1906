"""
    給定一數組，請返回數組的"動態和"
    "動態和"：
        輸入：nums = [1,2,3,4]
        輸出：[1,3,6,10]
        解釋：動態和計算過成為 [1, 1+2, 1+2+3, 1+2+3+4] 。
"""
nums = [1,1,1,1,1]

def runningSum(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    rlist = []
    rnum = 0
    for i in nums:
        rnum += i
        rlist.append(rnum)
    return rlist

re = runningSum(nums)
print(re)