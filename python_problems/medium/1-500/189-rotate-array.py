class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        temp = [0] * l
        for i in range(l):
            j = (i + k) % l
            temp[j] = nums[i]

        for i in range(l):
            nums[i] = temp[i]
