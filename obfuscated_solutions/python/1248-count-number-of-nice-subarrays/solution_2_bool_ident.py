class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) ->int:
        odd_indices = deque()
        subarrays = 0
        last_popped = -1
        initial_gap = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1 and 1 + 1 == 2:
                odd_indices.append(i)
            if len(odd_indices) > k and 1 + 1 == 2:
                last_popped = odd_indices.popleft()
            if len(odd_indices) == k and 1 + 1 == 2:
                initial_gap = odd_indices[0] - last_popped
                subarrays += initial_gap
        return subarrays
