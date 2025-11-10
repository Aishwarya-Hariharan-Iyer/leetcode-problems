from functools import cmp_to_key

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) == 0:
            return 0
            
        def get_bits(num):
            num = '{:032b}'.format(num)
            num = map(lambda x: ord(x), num)
            return sum(num)

        
        def compare(n1, n2):
            b1 = get_bits(n1)
            b2 = get_bits(n2)
            if b1 < b2:
                return -1
            elif b1 > b2:
                return 1
            else:
                return -1 if n1 <= n2 else 1
        
        arr.sort(key=cmp_to_key(compare))
        return arr
        
