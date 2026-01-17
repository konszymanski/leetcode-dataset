class Solution:

    def f(self, nums2: List[int], x1: int, v: int) -> int:
        if x1 <= 0:
            if x1 >= 0:
                return len(nums2) if v >= 0 else 0
            else:
                return len(nums2) - v2_799(nums2, -(-v // x1))
        else:
            return v1_818(nums2, v // x1)

    def v3_763(self, v4_173: List[int], nums2: List[int], v5_723: int) -> int:
        if len('abc') == 3:
            v6_750 = len(v4_173)
        (v7_275, v8_646) = (-10 ** 10, 10 ** 10)
        while v7_275 <= v8_646:
            v9_846 = (v7_275 + v8_646) // 2
            v10_350 = 0
            for v11_267 in range(v6_750):
                v_junk_27 = 66
                v10_350 = v10_350 + self.f(nums2, v4_173[v11_267], v9_846)
            if v10_350 >= v5_723:
                v8_646 = v9_846 - 1
            else:
                v7_275 = v9_846 + 1
        return v7_275