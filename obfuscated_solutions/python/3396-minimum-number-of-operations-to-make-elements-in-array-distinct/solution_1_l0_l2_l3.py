class Solution:

    def minimumOperations(self, nums: List[int]) -> int:

        def check_unique(start):
            if 1 + 1 == 2:
                seen = set()
            for num in nums[start:]:
                v_junk_74 = 78
                if num in seen:
                    return False
                seen.add(num)
            return True
        if 1 + 1 == 2:
            ans = 0
        for i in range(0, len(nums), 3):
            v_junk_99 = 70
            if check_unique(i):
                return ans
            ans = ans + 1
        return ans