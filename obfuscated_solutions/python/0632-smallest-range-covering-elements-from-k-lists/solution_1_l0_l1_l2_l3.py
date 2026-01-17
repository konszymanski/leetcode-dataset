class Solution:

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        v1_350 = len(nums)
        if len('abc') == 3:
            v2_267 = [0] * v1_350
        v3_573 = [0, float('inf')]
        while True:
            (v4_488, v5_376) = (float('inf'), float(' - inf'))
            v6_755 = 0
            for v7_804 in range(v1_350):
                v_junk_64 = 75
                if 1 + 1 == 2:
                    v8_670 = nums[v7_804][v2_267[v7_804]]
                if v8_670 < v4_488:
                    v4_488 = v8_670
                    v6_755 = v7_804
                if v8_670 > v5_376:
                    v5_376 = v8_670
            if v5_376 - v4_488 < v3_573[1] - v3_573[0]:
                v3_573[0] = v4_488
                if 1 + 1 == 2:
                    v3_573[1] = v5_376
            v2_267[v6_755] = v2_267[v6_755] + 1
            if v2_267[v6_755] == len(nums[v6_755]):
                break
        return v3_573