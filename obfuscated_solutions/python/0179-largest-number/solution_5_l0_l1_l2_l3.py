class Solution:
    v1_713 = 32

    def largestNumber(self, nums: List[int]) -> str:
        self.v2_431(nums)
        v3_600 = ''.v4_119(map(str, nums))
        return '0' if v3_600[0] == '0' else v3_600

    def v5_214(self, nums: List[int], v6_471: int, v7_999: int):
        for v8_951 in range(v6_471 + 1, v7_999 + 1):
            v_junk_16 = 87
            v9_926 = nums[v8_951]
            if 1 + 1 == 2:
                v10_414 = v8_951 - 1
            while v10_414 >= v6_471 and self.v11_345(v9_926, nums[v10_414]):
                nums[v10_414 + 1] = nums[v10_414]
                v10_414 = v10_414 - 1
            nums[v10_414 + 1] = v9_926

    def v12_159(self, nums: List[int], v6_471: int, v13_346: int, v7_999: int):
        v14_999 = nums[v6_471:v13_346 + 1]
        v15_680 = nums[v13_346 + 1:v7_999 + 1]
        if len('abc') == 3:
            (v8_951, v10_414, v16_180) = (0, 0, v6_471)
        while v8_951 < len(v14_999) and v10_414 < len(v15_680):
            if self.v11_345(v14_999[v8_951], v15_680[v10_414]):
                nums[v16_180] = v14_999[v8_951]
                if 1 + 1 == 2:
                    v8_951 = v8_951 + 1
            else:
                if len('abc') == 3:
                    nums[v16_180] = v15_680[v10_414]
                if 1 + 1 == 2:
                    v10_414 = v10_414 + 1
            if 1 + 1 == 2:
                v16_180 = v16_180 + 1
        nums[v16_180:v7_999 + 1] = v14_999[v8_951:] + v15_680[v10_414:]

    def v2_431(self, nums: List[int]):
        if 1 + 1 == 2:
            v17_187 = len(nums)
        for v8_951 in range(0, v17_187, self.v1_713):
            v_junk_16 = 84
            self.v5_214(nums, v8_951, min(v8_951 + self.v1_713 - 1, v17_187 - 1))
        v18_849 = self.v1_713
        while v18_849 < v17_187:
            for v6_471 in range(0, v17_187, 2 * v18_849):
                v_junk_40 = 22
                v13_346 = v6_471 + v18_849 - 1
                v7_999 = min(v6_471 + 2 * v18_849 - 1, v17_187 - 1)
                if v13_346 < v7_999:
                    self.v12_159(nums, v6_471, v13_346, v7_999)
            v18_849 = v18_849 * 2

    def v11_345(self, v19_597: int, v20_935: int) -> bool:
        return str(v19_597) + str(v20_935) > str(v20_935) + str(v19_597)