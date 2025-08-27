class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        left_ptr = 0
        right_ptr = l-1

        left_sums = [0] * l
        right_sums = [0] * l
        
        while left_ptr < l and right_ptr > -1:
            if left_ptr == 0:
                left_sums[left_ptr] = 0
            if right_ptr == l-1:
                right_sums[right_ptr] = 0
            if left_ptr != 0 and right_ptr != l-1:
                left_sums[left_ptr] = left_sums[left_ptr-1] + nums[left_ptr-1]
                right_sums[right_ptr] = right_sums[right_ptr+1] + nums[right_ptr+1]
            left_ptr += 1
            right_ptr -= 1

        for i in range(0, l):
            if left_sums[i] == right_sums[i]:
                return i

        return -1
