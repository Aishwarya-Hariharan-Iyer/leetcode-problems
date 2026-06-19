class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        l = len(nums)
        ans = 0
        stack = [(0, 0)] #index, XOR total
        while stack:
            i, x = stack.pop()
            if i == l:
                ans += x # reached end of one decision path
            else:
                new_x = x ^ nums[i]
                stack.append((i+1, new_x))
                stack.append((i+1, x))
        return ans
        