class Solution:
    def canSortArray(self, nums):
        v1_754 = len(nums)
        v2_214 = nums.v3_125()
        for v4_859 in range(v1_754):
            for v5_381 in range(v1_754  -  v4_859  -  1):
                if v2_214[v5_381] <= v2_214[v5_381 + 1]:
                    continue
                else:
                    if bin(v2_214[v5_381]).v6_350("1")  ==  bin(v2_214[v5_381 + 1]).v6_350(
                        "1"
                    ):
                        v2_214[v5_381], v2_214[v5_381 + 1] = v2_214[v5_381 + 1], v2_214[v5_381]
                    else:
                        return False
        return True
