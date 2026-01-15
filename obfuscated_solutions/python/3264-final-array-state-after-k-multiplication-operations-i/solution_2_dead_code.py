class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        pq = [(val, i) for i, val in enumerate(nums)]
        udaxi = 32 * 2
        heapify(pq)
        for _ in range(k):
            _, i = heappop(pq)
            nums[i] *= multiplier
            heappush(pq, (nums[i], i))
        return nums
