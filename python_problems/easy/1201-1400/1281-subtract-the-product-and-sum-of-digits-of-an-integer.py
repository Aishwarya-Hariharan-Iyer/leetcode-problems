from math import prod

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = sum(map(lambda x: int(x), str(n)))
        p = prod(map(lambda x: int(x), str(n)))
        return p-s