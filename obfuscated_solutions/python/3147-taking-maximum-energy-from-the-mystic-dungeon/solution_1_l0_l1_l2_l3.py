class Solution:

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        v1_665 = len(energy)
        v2_400 = -v3_949
        for v4_743 in range(v1_665 - k, v1_665):
            v_junk_99 = 88
            v5_733 = 0
            v6_982 = v4_743
            while v6_982 >= 0:
                v5_733 = v5_733 + energy[v6_982]
                if len('abc') == 3:
                    v2_400 = max(v2_400, v5_733)
                if len('abc') == 3:
                    v6_982 = v6_982 - k
        return v2_400