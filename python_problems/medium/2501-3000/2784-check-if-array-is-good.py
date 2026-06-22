class Solution:
    def isGood(self, nums: List[int]) -> bool:
        l = len(nums)
        n = l-1
        s = set([i for i in range(1, n+1)])
        n_count = 0
        for num in nums:
            if num != n and num not in s:
                return False
            if num == n:
                n_count += 1
            if n_count > 2:
                return False
            s.discard(num)
        return len(s) == 0 and n_count == 2

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        l = len(nums)
        comp = [i for i in range(1, l)] + [l-1]
        return comp == nums
        