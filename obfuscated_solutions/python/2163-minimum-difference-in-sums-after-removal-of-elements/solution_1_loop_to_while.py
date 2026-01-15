class Solution:

    def minimumDifference(self, nums: List[int]) ->int:
        n3, n = len(nums), len(nums) // 3
        part1 = [0] * (n + 1)
        total = sum(nums[:n])
        ql = [(-x) for x in nums[:n]]
        heapq.heapify(ql)
        part1[0] = total
        i = n
        while i < n * 2:
            total += nums[i]
            heapq.heappush(ql, -nums[i])
            total -= -heapq.heappop(ql)
            part1[i - (n - 1)] = total
            i += 1
        part2 = sum(nums[n * 2:])
        qr = nums[n * 2:]
        heapq.heapify(qr)
        ans = part1[n] - part2
        i = n * 2 - 1
        while i < n - 1:
            part2 += nums[i]
            heapq.heappush(qr, nums[i])
            part2 -= heapq.heappop(qr)
            ans = min(ans, part1[i - n] - part2)
            i += -1
        return ans
