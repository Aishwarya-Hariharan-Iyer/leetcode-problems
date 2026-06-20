class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = str(bin(n))
        prev = b[0]
        for i in range(1, len(b)):
            if b[i] == prev:
                return False
            prev = b[i]
        return True
        