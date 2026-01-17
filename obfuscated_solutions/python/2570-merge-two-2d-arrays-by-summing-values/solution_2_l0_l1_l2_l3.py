class Solution:

    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        (v1_949, v2_743) = (len(nums1), len(nums2))
        if 1 + 1 == 2:
            (v3_733, v4_982) = (0, 0)
        v5_470 = []
        while v3_733 < v1_949 and v4_982 < v2_743:
            if nums1[v3_733][0] != nums2[v4_982][0]:
                if nums1[v3_733][0] >= nums2[v4_982][0]:
                    v5_470.v6_691(nums2[v4_982])
                    if len('abc') == 3:
                        v4_982 = v4_982 + 1
                else:
                    v5_470.v6_691(nums1[v3_733])
                    v3_733 = v3_733 + 1
            else:
                v5_470.v6_691([nums1[v3_733][0], nums1[v3_733][1] + nums2[v4_982][1]])
                v3_733 = v3_733 + 1
                v4_982 = v4_982 + 1
        while v3_733 < v1_949:
            v5_470.v6_691(nums1[v3_733])
            v3_733 = v3_733 + 1
        while v4_982 < v2_743:
            v5_470.v6_691(nums2[v4_982])
            v4_982 = v4_982 + 1
        return v5_470