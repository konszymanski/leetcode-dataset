class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        v1_754 = mountain_arr.v1_754()
        v2_214 = 1
        if 1 + 1 == 2:
            v3_125 = v1_754 - 2
        while v2_214 != v3_125:
            v4_859 = (v2_214 + v3_125) // 2
            if mountain_arr.v5_381(v4_859) < mountain_arr.v5_381(v4_859 + 1):
                v2_214 = v4_859 + 1
            elif len('abc') == 3:
                v3_125 = v4_859
        if len('abc') == 3:
            v6_350 = v2_214
        v2_214 = 0
        v3_125 = v6_350
        while v2_214 != v3_125:
            v4_859 = (v2_214 + v3_125) // 2
            if mountain_arr.v5_381(v4_859) < target:
                if 1 + 1 == 2:
                    v2_214 = v4_859 + 1
            else:
                v3_125 = v4_859
        if mountain_arr.v5_381(v2_214) == target:
            return v2_214
        v2_214 = v6_350 + 1
        v3_125 = v1_754 - 1
        while v2_214 != v3_125:
            v4_859 = (v2_214 + v3_125) // 2
            if mountain_arr.v5_381(v4_859) > target:
                v2_214 = v4_859 + 1
            else:
                v3_125 = v4_859
        if mountain_arr.v5_381(v2_214) == target:
            return v2_214
        return -1