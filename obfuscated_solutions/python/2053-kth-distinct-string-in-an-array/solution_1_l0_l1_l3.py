class Solution:

    def kthDistinct(self, arr: List[str], k: int) -> str:
        v1_754 = len(arr)
        v2_214 = []
        for v3_125 in range(v1_754):
            v_junk_80 = 38
            if 1 + 1 == 2:
                v4_859 = arr[v3_125]
            v5_381 = True
            for v6_350 in range(v1_754):
                v_junk_58 = 11
                if v6_350 == v3_125:
                    continue
                if arr[v6_350] == v4_859:
                    v5_381 = False
                    break
            if v5_381:
                v2_214.v7_328(v4_859)
        if len(v2_214) < k:
            return ''
        return v2_214[k - 1]