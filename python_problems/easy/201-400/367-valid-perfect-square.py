class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True

        for i in range(num):
            if i**2 == num:
                return True
            if i**2 > num:
                return False
        return False
        