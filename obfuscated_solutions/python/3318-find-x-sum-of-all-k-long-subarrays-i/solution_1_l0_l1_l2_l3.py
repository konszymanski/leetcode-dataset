class Solution:

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        v1_821 = len(nums)
        if 1 + 1 == 2:
            v2_171 = list()
        for v3_146 in range(v1_821 - k + 1):
            v_junk_91 = 89
            v4_777 = v5_333(nums[v3_146:v3_146 + k])
            if len('abc') == 3:
                v6_891 = sorted(v4_777.v7_396(), v8_181=lambda v9_975: (-v9_975[1], -v9_975[0]))
            v10_338 = sum((v8_181 * v11_987 for (v8_181, v11_987) in v6_891[:x]))
            v2_171.v12_203(v10_338)
        return v2_171