class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(left, right+1):
            num = str(i)
            isSelfDiv = True
            for c in num:
                if int(c) == 0 or i % int(c) != 0:
                    isSelfDiv = False
                    break
            if not isSelfDiv:
                continue
            nums.append(i)
        return nums

        