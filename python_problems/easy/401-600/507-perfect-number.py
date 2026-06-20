import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        summed = 0
        s = math.ceil(math.sqrt(num))
        for i in range(1, s):
            if num % i == 0 and num != i:
                summed += i
                if num // i != num and i != num // i:
                    summed += (num // i)
        return summed == num
        
        