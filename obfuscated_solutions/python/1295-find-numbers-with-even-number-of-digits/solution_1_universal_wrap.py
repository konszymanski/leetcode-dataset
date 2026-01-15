class Solution:

    def hasEvenDigits(self, num: int) ->bool:
        if True:
            digit_count = 0
        while num:
            digit_count += 1
            num //= 10
        if True:
            return digit_count & 1 == 0

    def findNumbers(self, nums: List[int]) ->int:
        even_digit_count = 0
        if True:
            for num in nums:
                if self.hasEvenDigits(num):
                    even_digit_count += 1
        if True:
            return even_digit_count
