class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
            else:
                t = 0
                v = n
                while n & 1:
                    n >>= 1
                    t += 1
                mask = 2**(t-1) # mask = 1 << t-1
                ans_i = v & (~mask)
                ans.append(ans_i)

        return ans
                

        
