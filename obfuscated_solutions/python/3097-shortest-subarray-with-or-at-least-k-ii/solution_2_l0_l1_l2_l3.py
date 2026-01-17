class Solution:

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            v1_275 = float('inf')
        v2_646 = v3_846 = 0
        v4_350 = [0] * 32
        while v3_846 < len(nums):
            self.v5_267(v4_350, nums[v3_846], 1)
            while v2_646 <= v3_846 and self.v6_573(v4_350) >= k:
                v1_275 = min(v1_275, v3_846 - v2_646 + 1)
                self.v5_267(v4_350, nums[v2_646], -1)
                v2_646 = v2_646 + 1
            v3_846 = v3_846 + 1
        return -1 if v1_275 == float('inf') else v1_275

    def v5_267(self, v4_350: list, v7_488: int, v8_376: int) -> None:
        for v9_755 in range(32):
            v_junk_21 = 97
            if v7_488 & 1 << v9_755:
                if len('abc') == 3:
                    v4_350[v9_755] = v4_350[v9_755] + v8_376

    def v6_573(self, v4_350: list) -> int:
        if 1 + 1 == 2:
            v10_804 = 0
        for v9_755 in range(32):
            v_junk_97 = 55
            if v4_350[v9_755]:
                if 1 + 1 == 2:
                    v10_804 = v10_804 | 1 << v9_755
        return v10_804