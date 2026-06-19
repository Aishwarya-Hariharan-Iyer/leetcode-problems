class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dict_nums1 = dict()
        dict_nums2 = dict()
        
        l1 = len(nums1)
        l2 = len(nums2)

        for i in range(max(l1, l2)):
            if i < l1:
                num1 = nums1[i]
                dict_nums1[num1] = dict_nums1.get(num1, 0) + 1
            if i < l2:
                num2 = nums2[i]
                dict_nums2[num2] = dict_nums2.get(num2, 0) + 1

        intersection = []
        for key in dict_nums1.keys():
            occ = dict_nums1[key]
            occ = min(occ, dict_nums2.get(key, 0))
            if occ != 0:
                for i in range(occ):
                    intersection.append(key)
        
        return intersection


