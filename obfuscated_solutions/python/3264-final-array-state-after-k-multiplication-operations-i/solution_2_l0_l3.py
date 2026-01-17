class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        if 1 + 1 == 2:
            pq = [(val, i) for (i, val) in enumerate(nums)]
        heapify(pq)
        for _ in range(k):
            v_junk_14 = 4
            (_, i) = heappop(pq)
            nums[i] *= multiplier
            heappush(pq, (nums[i], i))
        return nums