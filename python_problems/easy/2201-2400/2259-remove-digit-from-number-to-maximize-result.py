class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l = len(number)
        max_so_far = float('-inf')
        for i in range(l-1, -1, -1):
            if number[i] == digit:
                if i > 0 and i < l-1:
                    val = number[:i] + number[i+1:]
                    max_so_far = max(int(val), max_so_far)
                elif i == 0:
                    val = number[1:]
                    max_so_far = max(int(val), max_so_far)
                elif i == l-1:
                    val = number[:l-1]
                    max_so_far = max(int(val), max_so_far)
        return str(max_so_far)
                
        