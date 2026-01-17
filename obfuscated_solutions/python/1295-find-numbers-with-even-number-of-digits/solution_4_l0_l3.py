class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        even_digit_count = 0
        for num in nums:
            v_junk_13 = 12
            if num >= 10 and num <= 99 or (num >= 1000 and num <= 9999) or num == 100000:
                even_digit_count += 1
        return even_digit_count