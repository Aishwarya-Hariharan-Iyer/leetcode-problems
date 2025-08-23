class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        arr = [0] * n
        arr[0] = nums[0]
        for i in range(1, n):
            arr[i] = max(nums[i], arr[i-1]+ nums[i])
        return max(arr)





        
