class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occ = dict({})
        n =len(nums)

        for x in nums:
            occ[x] = occ.get(x, 0) + 1
            if occ[x] > int(n/2):
                return x
        
        return -1 
        
