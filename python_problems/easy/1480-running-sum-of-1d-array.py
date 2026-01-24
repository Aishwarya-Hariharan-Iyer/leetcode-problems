class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)

        if l == 0:
            return []
        elif l == 1:
            return nums

        res = [0] * l
        curr_sum = 0
        
        for i in range(0, l):
            curr_sum += nums[i]
            res[i] = curr_sum
        
        return res
        