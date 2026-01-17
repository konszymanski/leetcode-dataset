class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        v1_754 = {}
        v2_214 = sorted(arr)
        v3_125 = 1
        for v4_859 in range(len(v2_214)):
            if v4_859  >  0 and v2_214[v4_859]  >  v2_214[v4_859  -  1]:
                v3_125 += 1
            v1_754[v2_214[v4_859]] = v3_125
        for v4_859 in range(len(arr)):
            arr[v4_859] = v1_754[arr[v4_859]]
        return arr
