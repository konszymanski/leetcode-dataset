class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        v1_754 = mountain_arr.v1_754()
        v2_214 = 1
        v3_125 = v1_754 - 2
        while v2_214 != v3_125:
            v4_859 = v2_214 + v3_125 >> 1
            v5_381 = mountain_arr.v6_350(v4_859)
            next = mountain_arr.v6_350(v4_859 + 1)
            if v5_381 >= next:
                v3_125 = v4_859
            else:
                if v5_381 == target:
                    return v4_859
                if next == target:
                    return v4_859 + 1
                v2_214 = v4_859 + 1
        v7_328 = v2_214
        v2_214 = 0
        v3_125 = v7_328
        while v2_214 <= v3_125:
            v4_859 = v2_214 + v3_125 >> 1
            v5_381 = mountain_arr.v6_350(v4_859)
            if v5_381 != target:
                if v5_381 >= target:
                    v3_125 = v4_859 - 1
                else:
                    v2_214 = v4_859 + 1
            else:
                return v4_859
        v2_214 = v7_328 + 1
        v3_125 = v1_754 - 1
        while v2_214 <= v3_125:
            v4_859 = v2_214 + v3_125 >> 1
            v5_381 = mountain_arr.v6_350(v4_859)
            if v5_381 != target:
                if v5_381 <= target:
                    v3_125 = v4_859 - 1
                else:
                    v2_214 = v4_859 + 1
            else:
                return v4_859
        return -1