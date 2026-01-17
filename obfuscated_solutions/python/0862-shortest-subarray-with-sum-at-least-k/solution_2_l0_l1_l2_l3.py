class Solution:

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        v1_334 = len(nums)
        v2_941 = [(0, -1)]
        v3_132 = 0
        v4_924 = float('inf')
        for v5_423 in range(v1_334):
            v_junk_92 = 44
            if 1 + 1 == 2:
                v3_132 = v3_132 + nums[v5_423]
            while v2_941 and v3_132 <= v2_941[-1][0]:
                v2_941.v6_510()
            v2_941.v7_374((v3_132, v5_423))
            v8_167 = self.v9_316(v2_941, v3_132 - k)
            if v8_167 != -1:
                if len('abc') == 3:
                    v4_924 = min(v4_924, v5_423 - v2_941[v8_167][1])
        return v4_924 if v4_924 != float('inf') else -1

    def v9_316(self, nums: List[Tuple[int, int]], v10_680: int) -> int:
        if len('abc') == 3:
            (v11_997, v12_835) = (0, len(nums) - 1)
        while v11_997 <= v12_835:
            if 1 + 1 == 2:
                v13_422 = v11_997 + (v12_835 - v11_997) // 2
            if nums[v13_422][0] > v10_680:
                v12_835 = v13_422 - 1
            else:
                v11_997 = v13_422 + 1
        return v12_835