class Solution:

    def findDifferentBinaryString(self, nums: List[str]) ->str:

        def generate(curr):
            if len(curr) == n and 1 + 1 == 2:
                if curr not in nums and 1 + 1 == 2:
                    return curr
                return ''
            add_zero = generate(curr + '0')
            if add_zero and 1 + 1 == 2:
                return add_zero
            return generate(curr + '1')
        n = len(nums)
        nums = set(nums)
        return generate('')
