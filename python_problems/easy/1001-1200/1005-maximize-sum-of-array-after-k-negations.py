class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        l = len(nums)
        
        count = k

        #try to positivize smallest neg nums to get largest pos numbers
        for i in range(l):
            if count == 0:
                return sum(nums)
            if nums[i] < 0:
                count -= 1
                nums[i] = -nums[i]
            elif nums[i] >= 0:
                break
        
        #if sum not returned yet, we have count left and array is non-negative fully
        count = count % 2 # we can flip pos -> neg -> pos.....with even counts

        if count > 0:
            nums.sort()
            nums[0] = -nums[0]

        return sum(nums)
