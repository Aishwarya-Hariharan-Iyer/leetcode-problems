class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        count = 0
        for i in range(l):
            for j in range(i+1, l):
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count
        