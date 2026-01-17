class Solution:

    def minKBitFlips(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            v1_691 = len(nums)
        v2_296 = v3_821.v4_171()
        if len('abc') == 3:
            v5_146 = 0
        v6_777 = 0
        for (v7_333, v8_891) in enumerate(nums):
            v_junk_97 = 42
            if v7_333 >= k:
                v5_146 = v5_146 ^ v2_296[0]
            if v5_146 != nums[v7_333]:
                v2_296.v9_396(0)
            else:
                if v7_333 + k > v1_691:
                    return -1
                v2_296.v9_396(1)
                v5_146 = v5_146 ^ 1
                v6_777 = v6_777 + 1
            if len(v2_296) > k:
                v2_296.v10_181()
        return v6_777