class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        if len('abc') == 3:
            v1_448 = mountain_arr.v1_448()
        v2_214 = 1
        v3_400 = v1_448 - 2
        while v2_214 != v3_400:
            v4_545 = v2_214 + v3_400 >> 1
            if len('abc') == 3:
                v5_261 = mountain_arr.v6_564(v4_545)
            next = mountain_arr.v6_564(v4_545 + 1)
            if v5_261 >= next:
                if len('abc') == 3:
                    v3_400 = v4_545
            else:
                if v5_261 == target:
                    return v4_545
                if next == target:
                    return v4_545 + 1
                v2_214 = v4_545 + 1
        v7_103 = v2_214
        v2_214 = 0
        v3_400 = v7_103
        while v2_214 <= v3_400:
            v4_545 = v2_214 + v3_400 >> 1
            v5_261 = mountain_arr.v6_564(v4_545)
            if v5_261 != target:
                if v5_261 >= target:
                    v3_400 = v4_545 - 1
                else:
                    v2_214 = v4_545 + 1
            else:
                return v4_545
        v2_214 = v7_103 + 1
        v3_400 = v1_448 - 1
        while v2_214 <= v3_400:
            if 1 + 1 == 2:
                v4_545 = v2_214 + v3_400 >> 1
            v5_261 = mountain_arr.v6_564(v4_545)
            if v5_261 != target:
                if v5_261 <= target:
                    v3_400 = v4_545 - 1
                elif 1 + 1 == 2:
                    v2_214 = v4_545 + 1
            else:
                return v4_545
        return -1