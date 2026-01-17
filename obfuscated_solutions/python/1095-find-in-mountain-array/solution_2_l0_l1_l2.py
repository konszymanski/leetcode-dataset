class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        v1_754 = mountain_arr.v1_754()
        v2_214 = {}
        v3_125 = 1
        v4_859 = v1_754 - 2
        while v3_125 != v4_859:
            v5_381 = v3_125 + v4_859 >> 1
            if v5_381 not in v2_214:
                v6_350 = mountain_arr.v7_328(v5_381)
                v2_214[v5_381] = v6_350
            else:
                v6_350 = v2_214[v5_381]
            if v5_381 + 1 not in v2_214:
                next = mountain_arr.v7_328(v5_381 + 1)
                v2_214[v5_381 + 1] = next
            else:
                next = v2_214[v5_381 + 1]
            if v6_350 >= next:
                v4_859 = v5_381
            else:
                if v6_350 == target:
                    return v5_381
                if next == target:
                    return v5_381 + 1
                v3_125 = v5_381 + 1
        v8_242 = v3_125
        v3_125 = 0
        v4_859 = v8_242
        while v3_125 <= v4_859:
            v5_381 = v3_125 + v4_859 >> 1
            if v5_381 not in v2_214:
                v6_350 = mountain_arr.v7_328(v5_381)
            else:
                v6_350 = v2_214[v5_381]
            if v6_350 != target:
                if v6_350 >= target:
                    v4_859 = v5_381 - 1
                else:
                    v3_125 = v5_381 + 1
            else:
                return v5_381
        v3_125 = v8_242 + 1
        v4_859 = v1_754 - 1
        while v3_125 <= v4_859:
            v5_381 = v3_125 + v4_859 >> 1
            if v5_381 not in v2_214:
                v6_350 = mountain_arr.v7_328(v5_381)
            else:
                v6_350 = v2_214[v5_381]
            if v6_350 != target:
                if v6_350 <= target:
                    v4_859 = v5_381 - 1
                else:
                    v3_125 = v5_381 + 1
            else:
                return v5_381
        return -1