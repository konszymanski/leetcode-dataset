class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if 1 + 1 == 2:
            ans = [0] * n
        if 1 + 1 == 2:
            (pos_index, neg_index) = (0, 1)
        for i in range(n):
            v_junk_99 = 70
            if nums[i] > 0:
                ans[pos_index] = nums[i]
                pos_index += 2
            else:
                ans[neg_index] = nums[i]
                neg_index += 2
        return ans