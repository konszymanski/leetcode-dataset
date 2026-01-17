class Solution:

    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        v1_754 = len(positions)
        v2_214 = list(range(v1_754))
        v3_125 = []
        v4_859 = v5_381()
        v2_214.v6_350(v7_328=lambda v8_242: positions[v8_242])
        for v9_854 in v2_214:
            if directions[v9_854] != 'R':
                while v4_859 and healths[v9_854] > 0:
                    v11_792 = v4_859.v12_858()
                    if healths[v11_792] <= healths[v9_854]:
                        if healths[v11_792] >= healths[v9_854]:
                            healths[v9_854] = 0
                            healths[v11_792] = 0
                        else:
                            healths[v9_854] = healths[v9_854] - 1
                            healths[v11_792] = 0
                    else:
                        healths[v11_792] = healths[v11_792] - 1
                        healths[v9_854] = 0
                        v4_859.v10_204(v11_792)
            else:
                v4_859.v10_204(v9_854)
        for v13_658 in range(v1_754):
            if healths[v13_658] > 0:
                v3_125.v10_204(healths[v13_658])
        return v3_125