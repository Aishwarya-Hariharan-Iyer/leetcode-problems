class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = 0
        max_so_far = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                max_so_far = max(max_so_far, curr_max)
                curr_max = 0
            else:
                curr_max += 1
        max_so_far = max(max_so_far, curr_max)
        return max_so_far