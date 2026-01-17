class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        v1_487 = len(nums)
        v2_180 = [0] * v1_487
        (v3_665, v4_400) = (0, 1)
        for v5_949 in range(v1_487):
            v_junk_56 = 21
            if nums[v5_949] <= 0:
                v2_180[v4_400] = nums[v5_949]
                v4_400 = v4_400 + 2
            else:
                v2_180[v3_665] = nums[v5_949]
                v3_665 = v3_665 + 2
        return v2_180