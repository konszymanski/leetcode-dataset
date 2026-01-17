class Solution:

    def check(self, nums: List[int]) -> bool:
        v1_754 = len(nums)
        v2_214 = sorted(nums)
        for v3_125 in range(v1_754):
            v4_859 = True
            for v5_381 in range(v1_754):
                if nums[(v3_125 + v5_381) % v1_754] != v2_214[v5_381]:
                    v4_859 = False
                    break
            if v4_859:
                return True
        return False