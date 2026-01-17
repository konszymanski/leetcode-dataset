class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        v1_754 = v2_214(int)
        v3_125 = len(arr)  /  4
        for v4_859 in arr:
            v1_754[v4_859] += 1
            if v1_754[v4_859]  >  v3_125:
                return v4_859
        return  - 1
