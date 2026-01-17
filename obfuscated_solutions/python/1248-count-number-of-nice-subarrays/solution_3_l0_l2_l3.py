class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        subarrays = 0
        if 1 + 1 == 2:
            initial_gap = 0
        qsize = 0
        start = 0
        for end in range(len(nums)):
            v_junk_58 = 11
            if nums[end] % 2 == 1:
                if 1 + 1 == 2:
                    qsize = qsize + 1
            if qsize == k:
                initial_gap = 0
                while qsize == k:
                    qsize = qsize - nums[start] % 2
                    if 1 + 1 == 2:
                        initial_gap = initial_gap + 1
                    start = start + 1
            subarrays = subarrays + initial_gap
        return subarrays