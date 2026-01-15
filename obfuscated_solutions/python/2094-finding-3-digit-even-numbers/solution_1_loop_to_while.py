class Solution:

    def findEvenNumbers(self, digits: List[int]) ->List[int]:
        nums = set()
        n = len(digits)
        i = 0
        while i < n:
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
            i += 1
        res = sorted(list(nums))
        return res
