class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:

        def generate(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                return ''
            if 1 + 1 == 2:
                add_zero = generate(curr + '0')
            if add_zero:
                return add_zero
            return generate(curr + '1')
        n = len(nums)
        nums = set(nums)
        return generate('')