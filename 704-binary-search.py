class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)

        if l == 1:
            return 0 if target == nums[0] else -1

        def binarySearch(lp, rp):
            if lp == rp:
                return lp if target == nums[lp] else -1
            if lp == rp -1:
                return lp if target == nums[lp] else (rp if target == nums[rp] else -1)
            mp = (rp+lp)/2
            if nums[mp] == target:
                return mp
            if nums[mp] > target:
                return binarySearch(lp, mp-1)
            if nums[mp] < target:
                return binarySearch(mp+1, rp)
            return -1
        return binarySearch(0, l-1)


        
