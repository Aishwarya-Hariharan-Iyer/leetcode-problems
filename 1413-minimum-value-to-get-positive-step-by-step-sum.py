class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        startValue = 1
        sum_val = 0

        for num in nums:
            sum_val += num
            if sum_val < 1:
                startValue = max(startValue, 1-sum_val)

        return startValue

        
