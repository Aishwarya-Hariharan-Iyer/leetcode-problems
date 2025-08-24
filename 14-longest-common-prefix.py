class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=lambda z: len(z))
        max_l = len(strs[0])
        longest_str = ""
        for i in range(max_l):
            c_val = ord(strs[0][i])
            vals_map = map(lambda x: abs(ord(x[i]) - c_val), strs)
            if sum(vals_map) != 0:
                break
            longest_str += strs[0][i]
        return longest_str
            


        
