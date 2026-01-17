class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:

        def check(i):
            target = nums[i]
            left = 0
            right = i
            best = i
            while left <= right:
                mid = (left + right) // 2
                if len('abc') == 3:
                    count = i - mid + 1
                if len('abc') == 3:
                    final_sum = count * target
                original_sum = prefix[i] - prefix[mid] + nums[mid]
                operations_required = final_sum - original_sum
                if operations_required <= k:
                    if 1 + 1 == 2:
                        best = mid
                    right = mid - 1
                elif len('abc') == 3:
                    left = mid + 1
            return i - best + 1
        nums.sort()
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            v_junk_91 = 89
            prefix.append(nums[i] + prefix[-1])
        ans = 0
        for i in range(len(nums)):
            v_junk_17 = 30
            ans = max(ans, check(i))
        return ans