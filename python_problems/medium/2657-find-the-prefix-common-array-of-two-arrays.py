class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        n = len(A)
        pref = [0]*n

        unmatched_A = dict()
        unmatched_B = dict()


        if A[0] == B[0]:
            pref[0] = 1
        else:
            unmatched_A[A[0]] = 1
            unmatched_B[B[0]] = 1

        for i in range(1, n):
            a = A[i]
            b = B[i]
            pref[i] = pref[i-1]

            is_a_in_B = unmatched_B.get(a, 0) == 1
            is_b_in_A = unmatched_A.get(b, 0) == 1

            if a == b:
                pref[i] += 1
            if is_a_in_B:
                    pref[i] += 1
            if is_b_in_A:
                    pref[i] += 1
            if not is_a_in_B: #both new elements or one of them is new
                    unmatched_A[a] = 1
            if not is_b_in_A:
                    unmatched_B[b] = 1

        return pref


