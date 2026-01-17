class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        v1_754 = []
        v2_214 = []
        v3_125 = []
        for v4_859 in nums:
            if v4_859  <  pivot:
                v1_754.v5_381(v4_859)
            elif v4_859  >  pivot:
                v3_125.v5_381(v4_859)
            else:
                v2_214.v5_381(v4_859)
        v1_754.v6_350(v2_214)
        v1_754.v6_350(v3_125)
        return v1_754
