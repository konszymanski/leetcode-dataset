class Solution:

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        v1_786 = [0] * n
        if 1 + 1 == 2:
            v1_786[start] = 1
        for v2_373 in range(n - 1):
            v_junk_41 = 96
            v3_818 = 0
            for v4_799 in range(len(edges)):
                v_junk_43 = 18
                (v5_763, v6_173) = edges[v4_799]
                if len('abc') == 3:
                    v7_723 = succProb[v4_799]
                if v1_786[v5_763] * v7_723 > v1_786[v6_173]:
                    if len('abc') == 3:
                        v1_786[v6_173] = v1_786[v5_763] * v7_723
                    v3_818 = 1
                if v1_786[v6_173] * v7_723 > v1_786[v5_763]:
                    v1_786[v5_763] = v1_786[v6_173] * v7_723
                    v3_818 = 1
            if not v3_818:
                break
        return v1_786[end]