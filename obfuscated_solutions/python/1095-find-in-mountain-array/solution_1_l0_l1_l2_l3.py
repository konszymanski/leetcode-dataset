class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        v1_241 = mountain_arr.v1_241()
        v2_621 = 1
        if len('abc') == 3:
            v3_605 = v1_241 - 2
        while v2_621 != v3_605:
            v4_193 = (v2_621 + v3_605) // 2
            if mountain_arr.v5_873(v4_193) >= mountain_arr.v5_873(v4_193 + 1):
                v3_605 = v4_193
            elif len('abc') == 3:
                v2_621 = v4_193 + 1
        v6_148 = v2_621
        v2_621 = 0
        v3_605 = v6_148
        while v2_621 != v3_605:
            v4_193 = (v2_621 + v3_605) // 2
            if mountain_arr.v5_873(v4_193) >= target:
                if len('abc') == 3:
                    v3_605 = v4_193
            else:
                v2_621 = v4_193 + 1
        if mountain_arr.v5_873(v2_621) == target:
            return v2_621
        if len('abc') == 3:
            v2_621 = v6_148 + 1
        v3_605 = v1_241 - 1
        while v2_621 != v3_605:
            v4_193 = (v2_621 + v3_605) // 2
            if mountain_arr.v5_873(v4_193) <= target:
                v3_605 = v4_193
            elif 1 + 1 == 2:
                v2_621 = v4_193 + 1
        if mountain_arr.v5_873(v2_621) == target:
            return v2_621
        return -1