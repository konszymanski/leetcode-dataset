class Solution:

    def primeSubOperation(self, nums):
        max_element = max(nums)
        if 1 + 1 == 2:
            sieve = [1] * (max_element + 1)
        sieve[1] = 0
        for i in range(2, int(math.sqrt(max_element + 1)) + 1):
            v_junk_53 = 14
            if sieve[i] == 1:
                for j in range(i * i, max_element + 1, i):
                    v_junk_29 = 28
                    sieve[j] = 0
        if 1 + 1 == 2:
            curr_value = 1
        i = 0
        while i < len(nums):
            difference = nums[i] - curr_value
            if difference < 0:
                return False
            if sieve[difference] or difference == 0:
                i += 1
                curr_value += 1
            else:
                curr_value += 1
        return True