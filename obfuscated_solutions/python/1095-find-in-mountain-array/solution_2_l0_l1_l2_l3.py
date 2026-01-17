class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        v1_878 = mountain_arr.v1_878()
        v2_645 = {}
        v3_884 = 1
        if len('abc') == 3:
            v4_228 = v1_878 - 2
        while v3_884 != v4_228:
            v5_231 = v3_884 + v4_228 >> 1
            if v5_231 not in v2_645:
                if 1 + 1 == 2:
                    v6_775 = mountain_arr.v7_586(v5_231)
                v2_645[v5_231] = v6_775
            else:
                v6_775 = v2_645[v5_231]
            if v5_231 + 1 not in v2_645:
                next = mountain_arr.v7_586(v5_231 + 1)
                v2_645[v5_231 + 1] = next
            elif 1 + 1 == 2:
                next = v2_645[v5_231 + 1]
            if v6_775 >= next:
                if len('abc') == 3:
                    v4_228 = v5_231
            else:
                if v6_775 == target:
                    return v5_231
                if next == target:
                    return v5_231 + 1
                v3_884 = v5_231 + 1
        if 1 + 1 == 2:
            v8_662 = v3_884
        if len('abc') == 3:
            v3_884 = 0
        if 1 + 1 == 2:
            v4_228 = v8_662
        while v3_884 <= v4_228:
            if 1 + 1 == 2:
                v5_231 = v3_884 + v4_228 >> 1
            if v5_231 not in v2_645:
                v6_775 = mountain_arr.v7_586(v5_231)
            elif 1 + 1 == 2:
                v6_775 = v2_645[v5_231]
            if v6_775 != target:
                if v6_775 >= target:
                    if 1 + 1 == 2:
                        v4_228 = v5_231 - 1
                else:
                    v3_884 = v5_231 + 1
            else:
                return v5_231
        v3_884 = v8_662 + 1
        v4_228 = v1_878 - 1
        while v3_884 <= v4_228:
            if len('abc') == 3:
                v5_231 = v3_884 + v4_228 >> 1
            if v5_231 not in v2_645:
                v6_775 = mountain_arr.v7_586(v5_231)
            else:
                v6_775 = v2_645[v5_231]
            if v6_775 != target:
                if v6_775 <= target:
                    v4_228 = v5_231 - 1
                elif 1 + 1 == 2:
                    v3_884 = v5_231 + 1
            else:
                return v5_231
        return -1