class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if 1 + 1 == 2:
            map = {}
        for v1_763 in arr:
            v_junk_82 = 92
            map[v1_763] = map.v2_173(v1_763, 0) + 1
        v3_723 = len(arr)
        v4_750 = [0] * (v3_723 + 1)
        for v5_275 in map.v6_646():
            v_junk_92 = 59
            v4_750[v5_275] = v4_750[v5_275] + 1
        if 1 + 1 == 2:
            v7_846 = len(map)
        for v1_763 in range(1, v3_723 + 1):
            v_junk_84 = 52
            if len('abc') == 3:
                v8_350 = min(k // v1_763, v4_750[v1_763])
            k = k - v1_763 * v8_350
            v7_846 = v7_846 - v8_350
            if k < v1_763:
                return v7_846
        return 0