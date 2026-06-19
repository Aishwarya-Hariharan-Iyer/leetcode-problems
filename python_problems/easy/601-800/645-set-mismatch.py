class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rep_num = 0
        n = len(nums)

        exp_sum = (n * (n+1))/2
        nums_cnt = dict()
        sum_arr = 0

        for i in range(n):
            count = nums_cnt.get(nums[i], 0) + 1
            if count == 2:
                rep_num = nums[i]
            nums_cnt[nums[i]] = count
            sum_arr += nums[i]

        sum_arr -= rep_num
        missing_num = exp_sum - sum_arr
        return [rep_num, missing_num]  