class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        result = [nums[0]] * l

        for i in range(l):
            new_i = (i + nums[i]) % l
            result[i] = nums[new_i]
        return result
