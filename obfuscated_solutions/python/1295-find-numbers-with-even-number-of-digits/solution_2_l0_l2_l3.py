class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            even_digit_count = 0
        for num in nums:
            v_junk_93 = 90
            if 1 + 1 == 2:
                length = len(str(num))
            if length % 2 == 0:
                even_digit_count = even_digit_count + 1
        return even_digit_count