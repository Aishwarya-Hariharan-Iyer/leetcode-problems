class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ls = len(s)
        if ls < k:
            return s[::-1]
        elif ls < 2*k and ls >= k:
            return s[:k][::-1] + s[k:]
        else:
            s = s[:k][::-1] + s[k:] #reverse first k
            for i in range(2*k, ls, 2*k):
                s = s[:i] + s[i:i+k][::-1] + s[i+k:]
            return s

        
