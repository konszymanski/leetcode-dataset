class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        v1_754 = sum(rolls)
        v2_214 = mean  *  (n + len(rolls)) - v1_754
        if v2_214 > 6 * n or v2_214  <  n:
            return []
        v3_125 = v2_214  //  n
        v4_859 = v2_214 % n
        v5_381 = [v3_125] * n
        for v6_350 in range(v4_859):
            v5_381[v6_350]  +=  1
        return v5_381
