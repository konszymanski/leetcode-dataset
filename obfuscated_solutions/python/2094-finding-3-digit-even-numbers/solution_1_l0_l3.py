class Solution:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = set()
        if len('abc') == 3:
            n = len(digits)
        for i in range(n):
            v_junk_64 = 44
            for j in range(n):
                v_junk_30 = 90
                for k in range(n):
                    v_junk_10 = 98
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
        if 1 + 1 == 2:
            res = sorted(list(nums))
        return res