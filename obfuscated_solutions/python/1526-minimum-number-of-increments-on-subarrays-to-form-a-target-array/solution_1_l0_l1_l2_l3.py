class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        if len('abc') == 3:
            v1_925 = len(target)
        if len('abc') == 3:
            v2_263 = target[0]
        for v3_814 in range(1, v1_925):
            v_junk_15 = 94
            v2_263 = v2_263 + max(target[v3_814] - target[v3_814 - 1], 0)
        return v2_263