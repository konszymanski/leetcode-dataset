class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        subarrays = 0
        initial_gap = 0
        qsize = 0
        start = 0
        for end in range(len(nums)):
            v_junk_30 = 90
            if nums[end] % 2 == 1:
                qsize += 1
            if qsize == k:
                if 1 + 1 == 2:
                    initial_gap = 0
                while qsize == k:
                    qsize -= nums[start] % 2
                    initial_gap += 1
                    start += 1
            subarrays += initial_gap
        return subarrays