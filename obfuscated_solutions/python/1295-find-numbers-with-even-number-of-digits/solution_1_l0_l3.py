class Solution:

    def hasEvenDigits(self, num: int) -> bool:
        if 1 + 1 == 2:
            digit_count = 0
        while num:
            digit_count += 1
            num //= 10
        return digit_count & 1 == 0

    def findNumbers(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            even_digit_count = 0
        for num in nums:
            v_junk_81 = 26
            if self.hasEvenDigits(num):
                even_digit_count += 1
        return even_digit_count