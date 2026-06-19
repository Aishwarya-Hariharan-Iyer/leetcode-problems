class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        l = len(nums)
        if l == 0:
            return 0
        lp = 1
        while lp < l:
            curr = nums[lp]
            prev = nums[lp-1]
            if curr <= prev:
                diff = abs(curr - prev) + 1
                ops += diff
                nums[lp] = curr + diff
            lp += 1
        return ops

