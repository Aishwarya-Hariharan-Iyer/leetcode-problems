class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        one_even = 0 # even 1s, odd 0s
        one_odd = 0 # odd 1s, even 0s
        for i in range(l):
            if (i % 2 == 0 and s[i] == '1') or (i % 2 == 1 and s[i] == '0'):
                one_odd += 1
            elif (i % 2 == 1 and s[i] == '1') or (i % 2 == 0 and s[i] == '0'):
                one_even += 1
        
        return min(one_even, one_odd)

        
