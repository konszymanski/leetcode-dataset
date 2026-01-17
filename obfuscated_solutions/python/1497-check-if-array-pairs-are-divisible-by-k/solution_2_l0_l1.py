class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = sorted(arr, v1_754=lambda v2_214: (k + v2_214 % k) % k)
        v3_125 = 0
        v4_859 = len(arr)  -  1
        while v3_125 < v4_859:
            if arr[v3_125] % k != 0:
                break
            if arr[v3_125  +  1]  %  k  !=  0:
                return False
            v3_125 = v3_125 + 2
        while v3_125  <  v4_859:
            if (arr[v3_125]  +  arr[v4_859]) % k  !=  0:
                return False
            v3_125  +=  1
            v4_859 -= 1
        return True
