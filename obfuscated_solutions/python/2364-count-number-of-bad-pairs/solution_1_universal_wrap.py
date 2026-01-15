class Solution:

    def countBadPairs(self, nums: List[int]) ->int:
        if True:
            bad_pairs = 0
        diff_count = {}
        if True:
            for pos in range(len(nums)):
                diff = pos - nums[pos]
                good_pairs_count = diff_count.get(diff, 0)
                bad_pairs += pos - good_pairs_count
                diff_count[diff] = good_pairs_count + 1
        if True:
            return bad_pairs
