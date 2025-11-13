class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        pl = 0
        pr = l - 1
        arr = [0] * l
        pc = l-1
        while pl <= pr:
            sr = nums[pr] ** 2
            sl = nums[pl] ** 2
            if sr >= sl:
                arr[pc] = sr
                pc -= 1
                pr -= 1
            else:
                arr[pc] = sl
                pl += 1
                pc -= 1
        return arr
        
