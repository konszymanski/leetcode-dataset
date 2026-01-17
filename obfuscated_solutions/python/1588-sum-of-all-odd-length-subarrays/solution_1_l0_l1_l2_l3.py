class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len('abc') == 3:
            v1_400 = len(arr)
        if len('abc') == 3:
            v2_949 = 0
        for v3_743 in range(v1_400):
            v_junk_41 = 21
            for v4_733 in range(v3_743, v1_400):
                v_junk_78 = 94
                if (v4_733 - v3_743 + 1) % 2 == 1:
                    if len('abc') == 3:
                        v5_982 = 0
                    for v6_470 in range(v3_743, v4_733 + 1):
                        v_junk_97 = 83
                        v5_982 = v5_982 + arr[v6_470]
                    if 1 + 1 == 2:
                        v2_949 = v2_949 + v5_982
        return v2_949