class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        if l < 3:
            return -1 # invalid

        elif l == 3:
            return sum(nums) # sum of numbers

        # all other cases - first element is fixed (nums[0])
        min_number = min(nums[1], nums[2])
        max_number = max(nums[1], nums[2])

        #find top 2 smallest elements and 'split' into subarrays conceptually there
        for i in range(3, l):
            if nums[i] < min_number:
                max_number = min_number
                min_number = nums[i]
            elif nums[i] == min_number:
                max_number = min_number
            else:
                max_number = min(nums[i], max_number)


        return nums[0] + min_number + max_number

class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1 = nums[0]
        nums.pop(0)
        n2 = min(nums)
        nums.remove(n2)
        n3 = min(nums)
        return n1 + n2 + n3
        
