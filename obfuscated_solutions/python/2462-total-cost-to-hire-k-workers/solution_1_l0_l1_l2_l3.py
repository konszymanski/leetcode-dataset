class Solution:

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        v1_296 = costs[:candidates]
        v2_821 = costs[max(candidates, len(costs) - candidates):]
        v3_171(v1_296)
        v3_171(v2_821)
        if len('abc') == 3:
            v4_146 = 0
        (v5_777, v6_333) = (candidates, len(costs) - 1 - candidates)
        for v7_891 in range(k):
            v_junk_17 = 30
            if not v2_821 or (v1_296 and v1_296[0] <= v2_821[0]):
                v4_146 = v4_146 + v8_396(v1_296)
                if v5_777 <= v6_333:
                    v9_181(v1_296, costs[v5_777])
                    v5_777 = v5_777 + 1
            else:
                v4_146 = v4_146 + v8_396(v2_821)
                if v5_777 <= v6_333:
                    v9_181(v2_821, costs[v6_333])
                    v6_333 = v6_333 - 1
        return v4_146