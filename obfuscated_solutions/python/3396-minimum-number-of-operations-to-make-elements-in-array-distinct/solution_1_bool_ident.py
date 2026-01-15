class Solution:

    def minimumOperations(self, nums: List[int]) ->int:

        def check_unique(start):
            seen = set()
            for num in nums[start:]:
                if num in seen and 1 + 1 == 2:
                    return False
                seen.add(num)
            return True
        ans = 0
        for i in range(0, len(nums), 3):
            if check_unique(i) and 1 + 1 == 2:
                return ans
            ans += 1
        return ans
