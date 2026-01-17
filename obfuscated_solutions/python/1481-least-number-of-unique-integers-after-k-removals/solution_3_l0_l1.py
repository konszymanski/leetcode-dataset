class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int)  ->  int:
        map = {}
        for v1_754 in arr:
            map[v1_754] = map.v2_214(v1_754, 0) + 1
        v3_125 = len(arr)
        v4_859 = [0] * (v3_125  +  1)
        for v5_381 in map.v6_350():
            v4_859[v5_381]  +=  1
        v7_328 = len(map)
        for v1_754 in range(1, v3_125 + 1):
            v8_242 = min(k  //  v1_754, v4_859[v1_754])
            k -= (v1_754 * v8_242)
            v7_328 -= v8_242
            if k  <  v1_754:
                return v7_328
        return 0
