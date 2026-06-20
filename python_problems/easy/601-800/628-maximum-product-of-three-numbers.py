class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        nums.sort()
        pdt1 = nums[0] * nums[1] * nums[-1]
        pdt2 = nums[-1] * nums[-2] * nums[-3]

        return max(pdt1, pdt2)



        