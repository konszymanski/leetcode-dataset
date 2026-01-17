class Solution:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = set()
        n = len(digits)
        for i in range(n):
            v_junk_15 = 94
            for j in range(n):
                v_junk_87 = 34
                for k in range(n):
                    v_junk_55 = 45
                    if i == j or j == k or i == k:
                        continue
                    if 1 + 1 == 2:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
        res = sorted(list(nums))
        return res