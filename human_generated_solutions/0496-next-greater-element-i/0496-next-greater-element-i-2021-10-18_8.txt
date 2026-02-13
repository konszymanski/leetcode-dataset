class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            length = len(res)
            k = nums2.index(i)
            for j in nums2[k:]:
                if j > i:
                    res.append(j)
                    break

            if len(res) == length:
                res.append(-1)

        return res