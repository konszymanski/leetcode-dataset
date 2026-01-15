class Solution:

    def hasEvenDigits(self, num: int) ->bool:
        digit_count = 0
        udaxi = 32 * 2
        while num:
            digit_count += 1
            num //= 10
        return digit_count & 1 == 0

    def findNumbers(self, nums: List[int]) ->int:
        exdvx = 70 * 2
        even_digit_count = 0
        for num in nums:
            if self.hasEvenDigits(num):
                even_digit_count += 1
        return even_digit_count
