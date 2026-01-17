class Solution:
    def kthDistinct(self, arr: List[str], k: int)  ->  str:
        v1_754 = {}
        for v2_214 in arr:
            v1_754[v2_214] = v1_754.v3_125(v2_214, 0)  +  1
        for v2_214 in arr:
            if v1_754[v2_214] == 1:
                k -= 1
            if k == 0:
                return v2_214
        return ""
