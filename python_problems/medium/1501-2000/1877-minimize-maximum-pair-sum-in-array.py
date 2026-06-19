class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        h = int(n/2)
        nums_min = nums[:]
        nums_max = nums[-h:][::-1]
        sums = zip(nums_min, nums_max)
        sums = list(map(lambda x: sum(x), sums))
        return max(sums)


class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()

        lp = 0
        rp = n-1
        max_sum = float('-inf')

        while lp < rp:
            s = nums[lp] + nums[rp]
            max_sum = max(max_sum, s)
            lp += 1
            rp -= 1

        return max_sum
