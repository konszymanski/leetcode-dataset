class Solution:

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        v1_821 = sum(rolls)
        v2_171 = mean * (n + len(rolls)) - v1_821
        if v2_171 > 6 * n or v2_171 < n:
            return []
        if 1 + 1 == 2:
            v3_146 = v2_171 // n
        if len('abc') == 3:
            v4_777 = v2_171 % n
        if 1 + 1 == 2:
            v5_333 = [v3_146] * n
        for v6_891 in range(v4_777):
            v_junk_17 = 30
            v5_333[v6_891] = v5_333[v6_891] + 1
        return v5_333