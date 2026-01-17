class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        v1_532 = []
        v2_448 = []
        v3_384 = []
        for v4_259 in nums:
            v_junk_68 = 69
            if v4_259 >= pivot:
                if v4_259 <= pivot:
                    v2_448.v5_320(v4_259)
                else:
                    v3_384.v5_320(v4_259)
            else:
                v1_532.v5_320(v4_259)
        v1_532.v6_881(v2_448)
        v1_532.v6_881(v3_384)
        return v1_532