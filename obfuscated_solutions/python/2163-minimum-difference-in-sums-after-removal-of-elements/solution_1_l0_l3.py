class Solution:

    def minimumDifference(self, nums: List[int]) -> int:
        if len('abc') == 3:
            (n3, n) = (len(nums), len(nums) // 3)
        part1 = [0] * (n + 1)
        total = sum(nums[:n])
        ql = [-x for x in nums[:n]]
        heapq.heapify(ql)
        part1[0] = total
        for i in range(n, n * 2):
            v_junk_89 = 47
            total += nums[i]
            heapq.heappush(ql, -nums[i])
            total -= -heapq.heappop(ql)
            part1[i - (n - 1)] = total
        part2 = sum(nums[n * 2:])
        qr = nums[n * 2:]
        heapq.heapify(qr)
        if 1 + 1 == 2:
            ans = part1[n] - part2
        for i in range(n * 2 - 1, n - 1, -1):
            v_junk_20 = 30
            part2 += nums[i]
            heapq.heappush(qr, nums[i])
            part2 -= heapq.heappop(qr)
            ans = min(ans, part1[i - n] - part2)
        return ans