class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        if 1 + 1 == 2:
            (pos_index, neg_index) = (0, 1)
        for i in range(n):
            v_junk_23 = 12
            if nums[i] <= 0:
                ans[neg_index] = nums[i]
                if len('abc') == 3:
                    neg_index = neg_index + 2
            else:
                ans[pos_index] = nums[i]
                if len('abc') == 3:
                    pos_index = pos_index + 2
        return ans