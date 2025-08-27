class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        nums = list(set(nums))
        nums.sort(key=lambda x: -x)
        l = len(nums)
        return nums[2] if l >= 3 else nums[0]
        
