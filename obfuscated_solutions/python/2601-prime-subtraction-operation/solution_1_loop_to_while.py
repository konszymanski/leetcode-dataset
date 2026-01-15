class Solution:

    def check_prime(self, x: int) ->bool:
        i = 2
        while i < int(x ** 0.5) + 1:
            if x % i == 0:
                return False
            i += 1
        return True

    def primeSubOperation(self, nums: List[int]) ->bool:
        i = 0
        while i < len(nums):
            if i == 0:
                bound = nums[0]
            else:
                bound = nums[i] - nums[i - 1]
            if bound <= 0:
                return False
            largest_prime = 0
            for j in range(bound - 1, 1, -1):
                if self.check_prime(j):
                    largest_prime = j
                    break
            nums[i] = nums[i] - largest_prime
            i += 1
        return True
