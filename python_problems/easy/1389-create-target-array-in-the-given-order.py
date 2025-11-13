class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        target = []
        for i in range(l):
            curr_l = len(target)
            ind = index[i]
            num = nums[i]
            temp = target[:ind] + [num] + target[ind:]
            target = temp


        return target
        
