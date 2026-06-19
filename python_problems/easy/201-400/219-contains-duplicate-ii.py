class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = len(nums)
        indices = dict()
        for i in range(l):
            indices[nums[i]] = indices.get(nums[i], []) + [i]
        
        for key in indices.keys():
            lv = len(indices[key])
            for x in range(1, lv):
                if indices[key][x] - indices[key][x-1] <= k:
                    return True
        
        return False
                
        
