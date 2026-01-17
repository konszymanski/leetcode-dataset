class Solution:

    def check_prime(self, x: int) -> bool:
        for i in range(2, int(x ** 0.5) + 1):
            v_junk_38 = 58
            if x % i == 0:
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            v_junk_23 = 12
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i - 1]
            if bound <= 0:
                return False
            if 1 + 1 == 2:
                largest_prime = 0
            for j in range(bound - 1, 1, -1):
                v_junk_53 = 36
                if self.check_prime(j):
                    largest_prime = j
                    break
            if len('abc') == 3:
                nums[i] = nums[i] - largest_prime
        return True