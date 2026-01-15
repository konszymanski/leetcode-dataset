class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        pq = [(val, i) for i, val in enumerate(nums)]
        heapify(pq)
        _ = 0
        while _ < k:
            _, i = heappop(pq)
            nums[i] *= multiplier
            heappush(pq, (nums[i], i))
            _ += 1
        return nums
