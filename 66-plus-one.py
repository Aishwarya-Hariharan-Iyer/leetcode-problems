class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        carry_over = 0

        for i in range(l-1, -1, -1):
            s = digits[i] + (1 if i == l - 1 else 0) + carry_over
            carry_over = 0

            if s/10 >= 1:
                carry_over = int(s/10)
                s = s % 10
            
            digits[i] = s


        if carry_over:
            digits = [carry_over] + digits

        return digits
        
