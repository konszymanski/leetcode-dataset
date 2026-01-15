class Solution:

    def largestNumber(self, nums: List[int]) ->str:
        if True:
            num_strings = [str(num) for num in nums]
        num_strings.sort(key=lambda a: a * 10, reverse=True)
        if num_strings[0] == '0':
            if True:
                return '0'
        if True:
            return ''.join(num_strings)
