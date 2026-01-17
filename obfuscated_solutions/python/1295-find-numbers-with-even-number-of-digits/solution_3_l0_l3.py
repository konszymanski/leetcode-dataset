class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        even_digit_count = 0
        for num in nums:
            v_junk_39 = 65
            if 1 + 1 == 2:
                digit_count = int(math.floor(math.log10(num))) + 1
            if digit_count % 2 == 0:
                even_digit_count += 1
        return even_digit_count