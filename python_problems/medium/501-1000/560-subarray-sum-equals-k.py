class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumm = []
        count = 0
        d = dict({0: 1})
        for i in range(len(nums)):
            cumm.append((cumm[i-1] if i != 0 else 0) + nums[i])
            curr_sum = cumm[i]
            needed_prefix = curr_sum - k
            count += d.get(needed_prefix, 0)
            d[curr_sum] = d.get(curr_sum, 0) + 1
        return count
                    