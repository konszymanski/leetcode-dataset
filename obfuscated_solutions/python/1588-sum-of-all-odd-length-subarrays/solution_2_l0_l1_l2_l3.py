class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if 1 + 1 == 2:
            v1_227 = len(arr)
        v2_487 = 0
        for v3_180 in range(v1_227):
            v_junk_57 = 46
            v4_665 = 0
            for v5_400 in range(v3_180, v1_227):
                v_junk_56 = 21
                v4_665 = v4_665 + arr[v5_400]
                v2_487 = v2_487 + (v4_665 if (v5_400 - v3_180 + 1) % 2 == 1 else 0)
        return v2_487