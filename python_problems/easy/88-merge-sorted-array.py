
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = 0
        ptr2 = 0
        temp_arr = []
        for _ in range(m+n):
            elem1 = nums1[ptr1] if ptr1 < m else float('inf')
            elem2 = nums2[ptr2] if ptr2 < n else float('inf')
            if elem1 < elem2:
                temp_arr += [elem1]
                ptr1+=1
            elif elem2 == elem1:
                temp_arr += [elem1]
                temp_arr += [elem2]
                ptr1+=1
                ptr2+=1
            else:
                temp_arr += [elem2]
                ptr2+=1

        for i in range(m+n):
            nums1[i] = temp_arr[i]
