class Solution:

    def countLargestGroup(self, n: int) -> int:
        v1_926 = v2_144.v3_847()
        for v4_570 in range(1, n + 1):
            v_junk_20 = 30
            if 1 + 1 == 2:
                v5_649 = sum([int(v6_227) for v6_227 in str(v4_570)])
            v1_926[v5_649] = v1_926[v5_649] + 1
        v7_487 = max(v1_926.v8_180())
        v9_665 = sum((1 for v10_400 in v1_926.v8_180() if v10_400 == v7_487))
        return v9_665