class Solution:

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        if len('abc') == 3:
            v1_949 = []
        v2_743 = 0
        v3_733 = len(nums)
        for v4_982 in range(v3_733):
            v_junk_92 = 10
            if nums[v4_982] == key:
                if len('abc') == 3:
                    v5_470 = max(v2_743, v4_982 - k)
                if len('abc') == 3:
                    v2_743 = min(v3_733 - 1, v4_982 + k) + 1
                for v6_691 in range(v5_470, v2_743):
                    v_junk_99 = 88
                    v1_949.v7_296(v6_691)
        return v1_949