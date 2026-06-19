class Solution(object):
    def get_min_sum_arr(self, nums, l):
        min_sum = nums[0] + nums[1]
        min_pair = [0, 1]
        for i in range(1, l):
            if nums[i] + nums[i-1] < min_sum:
                min_sum = nums[i] + nums[i-1]
                min_pair = [i-1, i]
        return nums[:min_pair[0]] + [min_sum] + nums[min_pair[1]+1:]
    
    def isNonDecreasing(self, nums, l):
        for i in range(1, l):
            if nums[i] < nums[i-1]:
                return False
        return True

    def minPairHelper(self, nums, count):

        l = len(nums)

        if l == 1 or self.isNonDecreasing(nums, l):
            return count
        
        updatedArr = self.get_min_sum_arr(nums, l)
        return self.minPairHelper(updatedArr, count+1)
            
    def minimumPairRemoval(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.minPairHelper(nums, 0)
        
        
