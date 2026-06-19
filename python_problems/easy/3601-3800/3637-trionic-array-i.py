class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        swaps = 0
        curr = 1 #1 for inc, -1 for dec
        l = len(nums)

        if l <= 3:
            return False

        if nums[1] <= nums[0]:
            return False

        for i in range(1, l):

            if nums[i] == nums[i-1]:
                return False # Strictness violated

            if curr == 1 and nums[i] - nums[i-1] < 0: # increases then dec
                swaps += 1
                curr = -1
            
            if curr == -1 and nums[i] - nums[i-1] > 0: # decreases then inc
                swaps += 1
                curr = 1


        return swaps == 2




        
