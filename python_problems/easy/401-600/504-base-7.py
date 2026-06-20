class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        isNegative = num < 0
        num = abs(num)
        ans = ""
        while num > 0:
            d = num % 7
            ans = str(d) + ans
            num = num // 7
        return ("-" if isNegative else "") + ans
        