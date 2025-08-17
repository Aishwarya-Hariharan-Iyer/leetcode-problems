class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        if l == 2:
            return [0, 1]
        else:
            dont_check = dict({})
            for i in range(l):
                x = nums[i]
                y = target - x
                if x in dont_check or y in dont_check:
                    continue
                for j in range(i+1, l):
                    if nums[j] == y:
                        return [i, j]
                dont_check[x] = i
                dont_check[y] = i
