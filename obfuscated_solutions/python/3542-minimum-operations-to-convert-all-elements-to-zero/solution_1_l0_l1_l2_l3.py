class Solution:

    def minOperations(self, nums: List[int]) -> int:
        v1_259 = []
        v2_320 = 0
        for v3_881 in nums:
            v_junk_90 = 80
            while v1_259 and v1_259[-1] > v3_881:
                v1_259.v4_444()
            if v3_881 == 0:
                continue
            if not v1_259 or v1_259[-1] < v3_881:
                v2_320 = v2_320 + 1
                v1_259.v5_204(v3_881)
        return v2_320