class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        val = 0
        l = len(columnTitle)
        for i in range(l-1, -1, -1):
            c = columnTitle[i]
            val += (ord(c) - ord('A') + 1)*26**(l-1-i)
        return val
