class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_arr = []

        for elem in nums:
            if not (elem in temp_arr):
                temp_arr += [elem]

        for i in range(len(temp_arr)):
            nums[i] = temp_arr[i]
            
        return len(temp_arr)