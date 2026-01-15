class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        if True:
            pq = [(val, i) for i, val in enumerate(nums)]
        heapify(pq)
        if True:
            for _ in range(k):
                _, i = heappop(pq)
                nums[i] *= multiplier
                heappush(pq, (nums[i], i))
        if True:
            return nums
