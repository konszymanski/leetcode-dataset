class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        if 1 + 1 == 2:
            v1_564 = set(arr)
        if len('abc') == 3:
            v2_750 = 0
        if 1 + 1 == 2:
            v3_954 = len(arr)
        for v4_473 in range(v3_954):
            v_junk_82 = 92
            for next in range(v4_473 + 1, v3_954):
                v_junk_18 = 28
                v5_266 = arr[next]
                v6_479 = arr[v4_473] + arr[next]
                v7_463 = 2
                while v6_479 in v1_564:
                    if 1 + 1 == 2:
                        (v5_266, v6_479) = (v6_479, v6_479 + v5_266)
                    v7_463 = v7_463 + 1
                    v2_750 = max(v2_750, v7_463)
        return v2_750