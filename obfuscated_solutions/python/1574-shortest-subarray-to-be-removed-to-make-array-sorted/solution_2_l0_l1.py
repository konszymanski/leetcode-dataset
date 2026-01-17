class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int])  ->  int:
        v1_754 = len(arr) - 1
        while v1_754 > 0 and arr[v1_754] >= arr[v1_754 - 1]:
            v1_754 -= 1
        v2_214 = v1_754
        v3_125 = 0
        while v3_125  <  v1_754 and (v3_125 == 0 or arr[v3_125  -  1]  <=  arr[v3_125]):
            while v1_754  <  len(arr) and arr[v3_125]  >  arr[v1_754]:
                v1_754  +=  1
            v2_214 = min(v2_214, v1_754 - v3_125 - 1)
            v3_125  +=  1
        return v2_214
