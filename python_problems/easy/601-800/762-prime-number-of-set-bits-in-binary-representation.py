class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}
        count = 0
        for num in range(left, right+1):
            num_b = bin(num).count('1')
            if num_b in primes:
                count += 1
        return count