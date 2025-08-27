class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """

        while len(nums) != 0:
            if original in nums:
                original *= 2
                nums = filter(lambda x: x % original == 0, nums)
            else:
                break
        
        return original


        
