class Solution:

    def minimumOperations(self, nums: List[int]) ->int:

        def check_unique(start):
            seen = set()
            for num in nums[start:]:
                if num in seen:
                    return False
                seen.add(num)
            return True
        ans = 0
        i = 0
        while i < len(nums):
            if check_unique(i):
                return ans
            ans += 1
            i += 3
        return ans
