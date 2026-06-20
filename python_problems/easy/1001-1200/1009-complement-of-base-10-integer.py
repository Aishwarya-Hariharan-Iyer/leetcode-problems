class Solution:
    def bitwiseComplement(self, n: int) -> int:
        nt = list(str(bin(n)[2:]))
        for i in range(len(nt)):
            if nt[i] == '0':
                nt[i] = '1'
            else:
                nt[i] = '0'
        return int(''.join(nt), 2)
        