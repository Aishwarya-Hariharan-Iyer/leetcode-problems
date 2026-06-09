class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l < 2:
            return 0
        
        boundary_arrays = []
        curr_char = s[0]
        curr_count = 1

        for i in range(1, l+1):
            if i == l:
                pair = [curr_char, curr_count]
                boundary_arrays += [pair]
            elif s[i] == curr_char:
                curr_count += 1
            else:
                pair = [curr_char, curr_count]
                curr_char = s[i]
                curr_count = 1
                boundary_arrays += [pair]

        b_len = len(boundary_arrays)

        if b_len <= 1:
            return 0
        
        count = 0
        for p in range(1, b_len):
            b_c1 = boundary_arrays[p][1]
            b_c2 = boundary_arrays[p-1][1]
            count += min(b_c1, b_c2)

        return count














#  class Solution(object): (O(n^2) - too large)

#     def isValidSubstring(self, s):
#         l = len(s)
#         if l < 2:
#             return False
#         if l % 2 == 1:
#             return False

#         cl = s[0]
#         cr = s[-1]

#         if cl == cr:
#             return False

#         l_end_ptr = l/2
#         l_sum = sum(s[:l_end_ptr]) 

#         if l_sum != cl * l/2:
#             return False

#         return sum(s[l_end_ptr:]) == cr * l/2


#     def countBinarySubstrings(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         l = len(s)
#         s = [int(c) for c in s]
#         count = 0
#         for i in range(l-1):
#             for j in range(i, l):
#                 if self.isValidSubstring(s[i:j+1]):
#                     count += 1
#         return count

        
