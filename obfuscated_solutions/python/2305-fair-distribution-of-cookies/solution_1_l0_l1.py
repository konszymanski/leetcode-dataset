class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        v1_754 = [0]  *  k
        v2_214 = len(cookies)
        def v3_125(v4_859, v5_381):
            if v2_214  -  v4_859  <  v5_381:
                return float('inf')
            if v4_859 == v2_214:
                return max(v1_754)
            v6_350 = float('inf')
            for v7_328 in range(k):
                v5_381  -=  int(v1_754[v7_328]  ==  0)
                v1_754[v7_328]  +=  cookies[v4_859]
                v6_350 = min(v6_350, v3_125(v4_859  +  1, v5_381))
                v1_754[v7_328] -= cookies[v4_859]
                v5_381 += int(v1_754[v7_328] == 0)
            return v6_350
        return v3_125(0, k)
