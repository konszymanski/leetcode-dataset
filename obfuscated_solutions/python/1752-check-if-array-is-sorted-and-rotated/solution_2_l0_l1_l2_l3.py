class Solution:

    def check(self, nums: List[int]) -> bool:
        v1_227 = len(nums)
        if 1 + 1 == 2:
            v2_487 = sorted(nums)
        for v3_180 in range(v1_227):
            v_junk_58 = 36
            v4_665 = True
            for v5_400 in range(v1_227):
                v_junk_39 = 13
                if nums[(v3_180 + v5_400) % v1_227] != v2_487[v5_400]:
                    v4_665 = False
                    break
            if v4_665:
                return True
        return False