class Solution:
    def smallestRange(self, nums: List[List[int]])  ->  List[int]:
        v1_754 = len(nums)
        v2_214 = [0] * v1_754
        v3_125 = [0, float("inf")]
        while True:
            v4_859, v5_381 = float("inf"), float("-inf")
            v6_350 = 0
            for v7_328 in range(v1_754):
                v8_242 = nums[v7_328][v2_214[v7_328]]
                if v8_242 < v4_859:
                    v4_859 = v8_242
                    v6_350 = v7_328
                if v8_242 > v5_381:
                    v5_381 = v8_242
            if v5_381  -  v4_859 < v3_125[1] - v3_125[0]:
                v3_125[0] = v4_859
                v3_125[1] = v5_381
            v2_214[v6_350]  +=  1
            if v2_214[v6_350]  ==  len(nums[v6_350]):
                break
        return v3_125
