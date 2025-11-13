class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l == 1:
            return nums

        p = 0
        while p < l:
            if nums[p] == 0:
                break
            p += 1
        

        for i in range(l):
            if p > i or p >= l:
                break
            if nums[i] != 0:
                nums[p] = nums[i]
                nums[i] = 0
                p += 1

        return nums


        