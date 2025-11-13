class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        l = len(s)

        mapping_st = dict({})
        mapping_ts = dict({})

        for i in range(l):

            c_s = s[i]
            c_t = t[i]
            c_map_st = mapping_st.get(c_s, '')
            c_map_ts = mapping_ts.get(c_t, '')

            if c_map_st == '':
                mapping_st[c_s] = c_t
            if c_map_ts == '':
                mapping_ts[c_t] = c_s

            if c_map_st != c_t and c_map_st != '':
                return False
            
            if c_map_ts != c_s and c_map_ts != '':
                return False

        return True
        
