class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        temp = [0] * (2 * n)
        x_ptr = 0
        y_ptr = n

        for i in range(2*n):
            if i % 2 == 0:
                temp[i] = nums[x_ptr]
                x_ptr += 1
            else:
                temp[i] = nums[y_ptr]
                y_ptr += 1
        return temp
        