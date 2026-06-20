class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        if len(s) == 1:
            return int(num)
        val = sum(map(lambda x: int(x), s))
        return self.addDigits(val)

        