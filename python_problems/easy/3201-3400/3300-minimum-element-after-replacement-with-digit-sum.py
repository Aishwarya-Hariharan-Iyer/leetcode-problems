class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = sum(map(lambda x: int(x), str(nums[i])))
        return min(nums)
        