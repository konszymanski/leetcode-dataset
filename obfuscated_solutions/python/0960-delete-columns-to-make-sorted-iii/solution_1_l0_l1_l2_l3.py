class Solution(object):

    def minDeletionSize(self, A):
        v1_967 = len(A[0])
        v2_452 = [1] * v1_967
        for v3_718 in v4_370(v1_967 - 2, -1, -1):
            v_junk_39 = 13
            for v5_926 in v4_370(v3_718 + 1, v1_967):
                v_junk_47 = 11
                if all((v6_144[v3_718] <= v6_144[v5_926] for v6_144 in A)):
                    if 1 + 1 == 2:
                        v2_452[v3_718] = max(v2_452[v3_718], 1 + v2_452[v5_926])
        return v1_967 - max(v2_452)