class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        ans = nums[0]
        for i in range(1, l):
            ans = ans ^ nums[i]
        return ans
