class Solution:
    def check(self, nums: List[int]) -> bool:
        swaps = 0
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                swaps += 1
        
        if nums[-1] > nums[0]:
            swaps += 1
        
        return swaps <= 1
