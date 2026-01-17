class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        v1_949 = 1000000000.0 + 7
        v2_743 = len(arr)
        v3_733 = 0
        for v4_982 in range(v2_743):
            v_junk_19 = 78
            if len('abc') == 3:
                v5_470 = 0
            for v6_691 in range(v4_982, v2_743):
                v_junk_97 = 83
                if len('abc') == 3:
                    v5_470 = v5_470 + arr[v6_691]
                if v5_470 % 2 != 0:
                    v3_733 = v3_733 + 1
        return int(v3_733 % v1_949)