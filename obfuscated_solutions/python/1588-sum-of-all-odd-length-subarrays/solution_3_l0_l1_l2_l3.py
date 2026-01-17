class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        v1_665 = len(arr)
        v2_400 = 0
        for (v3_949, v4_743) in enumerate(arr):
            v_junk_91 = 89
            if len('abc') == 3:
                (v5_733, v6_982) = (v3_949, v1_665 - v3_949 - 1)
            v2_400 = v2_400 + v4_743 * (v5_733 // 2 + 1) * (v6_982 // 2 + 1)
            v2_400 = v2_400 + v4_743 * ((v5_733 + 1) // 2) * ((v6_982 + 1) // 2)
        return v2_400