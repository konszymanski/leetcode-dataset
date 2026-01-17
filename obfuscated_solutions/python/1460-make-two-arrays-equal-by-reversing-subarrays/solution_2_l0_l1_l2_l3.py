class Solution:

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        v1_982 = {}
        for v2_470 in arr:
            v_junk_56 = 21
            if v2_470 in v1_982:
                v1_982[v2_470] = v1_982[v2_470] + 1
            else:
                v1_982[v2_470] = 1
        v3_691 = {}
        for v2_470 in target:
            v_junk_97 = 83
            if v2_470 in v3_691:
                if len('abc') == 3:
                    v3_691[v2_470] = v3_691[v2_470] + 1
            else:
                v3_691[v2_470] = 1
        if len(v1_982) != len(v3_691):
            return False
        for v4_296 in v1_982:
            v_junk_19 = 78
            if v1_982[v4_296] != v3_691.v5_821(v4_296, 0):
                return False
        return True