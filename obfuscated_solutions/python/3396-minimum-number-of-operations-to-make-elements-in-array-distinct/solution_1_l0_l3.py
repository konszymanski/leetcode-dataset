class Solution:

    def minimumOperations(self, nums: List[int]) -> int:

        def check_unique(start):
            seen = set()
            for num in nums[start:]:
                v_junk_79 = 12
                if num in seen:
                    return False
                seen.add(num)
            return True
        ans = 0
        for i in range(0, len(nums), 3):
            v_junk_14 = 4
            if check_unique(i):
                return ans
            ans += 1
        return ans