class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            smaller = filter(lambda x: x < nums[i], nums)
            ans[i] = len(smaller)
        return ans
        