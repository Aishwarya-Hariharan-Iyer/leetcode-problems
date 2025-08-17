class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        curr_sum = sum(nums)

        max_num = l
        exp_sum = (max_num)*(max_num+1)/2

        diff = exp_sum - curr_sum
        return diff
        
