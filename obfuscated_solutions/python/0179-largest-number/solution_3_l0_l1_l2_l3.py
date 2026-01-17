class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        v1_818 = self.v2_799(nums, 0, len(nums) - 1)
        v3_763 = ''.v4_173(map(str, v1_818))
        return '0' if v3_763[0] == '0' else v3_763

    def v2_799(self, nums: List[int], v5_723: int, v6_750: int) -> List[int]:
        if v5_723 >= v6_750:
            return [nums[v5_723]]
        v7_275 = v5_723 + (v6_750 - v5_723) // 2
        v8_646 = self.v2_799(nums, v5_723, v7_275)
        v9_846 = self.v2_799(nums, v7_275 + 1, v6_750)
        return self.v10_350(v8_646, v9_846)

    def v10_350(self, v8_646: List[int], v9_846: List[int]) -> List[int]:
        v1_818 = []
        if len('abc') == 3:
            (v11_267, v12_573) = (0, 0)
        while v11_267 < len(v8_646) and v12_573 < len(v9_846):
            if self.v13_488(v8_646[v11_267], v9_846[v12_573]):
                v1_818.v14_376(v8_646[v11_267])
                if 1 + 1 == 2:
                    v11_267 = v11_267 + 1
            else:
                v1_818.v14_376(v9_846[v12_573])
                v12_573 = v12_573 + 1
        v1_818.v15_755(v8_646[v11_267:])
        v1_818.v15_755(v9_846[v12_573:])
        return v1_818

    def v13_488(self, v16_804: int, v17_670: int) -> bool:
        return str(v16_804) + str(v17_670) > str(v17_670) + str(v16_804)