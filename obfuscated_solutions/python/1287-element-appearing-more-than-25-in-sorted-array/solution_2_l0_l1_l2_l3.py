class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        v1_877 = v2_925(int)
        v3_263 = len(arr) / 4
        for v4_814 in arr:
            v_junk_43 = 6
            v1_877[v4_814] = v1_877[v4_814] + 1
            if v1_877[v4_814] > v3_263:
                return v4_814
        return -1