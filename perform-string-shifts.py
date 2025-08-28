class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        def left_shift(s, l, n):
            i = n % l
            to_add = s[:i]
            return s[i:] + to_add
        
        def right_shift(s, l, n):
            i =  n % l
            to_add = s[l-i:]
            return to_add + s[:l-i]

        l = len(s)

        if l == 1:
            return s
        
        for command in shift:
            print(s)
            if command[0] == 0:
                s = left_shift(s, l, command[1])
            else:
                s = right_shift(s, l, command[1])

        return s
        
