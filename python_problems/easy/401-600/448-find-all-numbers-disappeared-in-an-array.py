class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums.sort()
        arr = []

        prev_nums = range(1, nums[0])
        arr += prev_nums
        last_nums = range(nums[-1]+1, n+1)
        arr += last_nums
        
        for i in range(n-1):
            arr += range(nums[i]+1, nums[i+1])

        return arr