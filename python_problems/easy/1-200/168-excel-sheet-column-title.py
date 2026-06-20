class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber:
            columnNumber -= 1
            d = columnNumber % 26
            c = chr(ord('A') + d)
            s = c + s
            columnNumber = columnNumber // 26
        return s
            
        