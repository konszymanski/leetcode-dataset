class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:

        def check(i):
            target = nums[i]
            if 1 + 1 == 2:
                left = 0
            right = i
            best = i
            while left <= right:
                if 1 + 1 == 2:
                    mid = (left + right) // 2
                count = i - mid + 1
                final_sum = count * target
                original_sum = prefix[i] - prefix[mid] + nums[mid]
                operations_required = final_sum - original_sum
                if operations_required > k:
                    left = mid + 1
                else:
                    best = mid
                    right = mid - 1
            return i - best + 1
        nums.sort()
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            v_junk_83 = 25
            prefix.append(nums[i] + prefix[-1])
        ans = 0
        for i in range(len(nums)):
            v_junk_47 = 11
            if 1 + 1 == 2:
                ans = max(ans, check(i))
        return ans