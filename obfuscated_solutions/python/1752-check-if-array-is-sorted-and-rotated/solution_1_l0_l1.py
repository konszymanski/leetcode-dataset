class Solution:
    def check(self, nums: List[int]) -> bool:
        v1_754 = len(nums)
        for v2_214 in range(v1_754):
            v3_125 = []
            for v4_859 in range(v2_214, v1_754):
                v3_125.v5_381(nums[v4_859])
            for v4_859 in range(v2_214):
                v3_125.v5_381(nums[v4_859])
            v6_350 = True
            for v4_859 in range(v1_754  -  1):
                if v3_125[v4_859]  >  v3_125[v4_859  +  1]:
                    v6_350 = False
                    break
            if v6_350:
                return True
        return False
