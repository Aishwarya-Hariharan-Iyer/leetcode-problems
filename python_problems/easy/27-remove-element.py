class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        temp_arr = []
        for elem in nums:
            if elem != val:
                count+=1
                temp_arr+=[elem]
        for i in range(count):
            nums[i] = temp_arr[i]

        return count