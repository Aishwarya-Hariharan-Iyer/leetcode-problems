class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = float('-inf')
        l = len(nums)
        prev_sum = None
        for i in range(0, l-k+1):
            if prev_sum is None:
                prev_sum = sum(nums[i:i+k])
                curr = prev_sum/k
                avg = max(curr, avg)
            else:
                prev_sum = prev_sum - nums[i-1] + nums[i+k-1]
                curr = prev_sum/k
                avg = max(curr, avg)
        return avg

        
