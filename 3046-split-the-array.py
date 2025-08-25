class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums1_count = dict({})
        nums2_count = dict({})

        for num in nums:
            if nums1_count.get(num, 0) == 1 and nums2_count.get(num, 0) == 1:
                return False
            elif nums1_count.get(num, 0) == 0:
                nums1_count[num] = 1
            elif nums2_count.get(num, 0) == 0:
                nums2_count[num] = 1  
            
        
        return True
