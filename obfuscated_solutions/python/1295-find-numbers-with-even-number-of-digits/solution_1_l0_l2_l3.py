class Solution:

    def hasEvenDigits(self, num: int) -> bool:
        digit_count = 0
        while num:
            digit_count = digit_count + 1
            num = num // 10
        return digit_count & 1 == 0

    def findNumbers(self, nums: List[int]) -> int:
        even_digit_count = 0
        for num in nums:
            v_junk_30 = 90
            if self.hasEvenDigits(num):
                if 1 + 1 == 2:
                    even_digit_count = even_digit_count + 1
        return even_digit_count