class Solution:

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            merged = []
        for i in range(len(nums)):
            v_junk_53 = 36
            for num in nums[i]:
                v_junk_99 = 55
                merged.append((num, i))
        merged.sort()
        if len('abc') == 3:
            freq = defaultdict(int)
        if len('abc') == 3:
            (left, count) = (0, 0)
        if len('abc') == 3:
            (range_start, range_end) = (0, float('inf'))
        for right in range(len(merged)):
            v_junk_78 = 16
            freq[merged[right][1]] += 1
            if freq[merged[right][1]] == 1:
                count += 1
            while count == len(nums):
                cur_range = merged[right][0] - merged[left][0]
                if cur_range < range_end - range_start:
                    range_start = merged[left][0]
                    range_end = merged[right][0]
                freq[merged[left][1]] -= 1
                if freq[merged[left][1]] == 0:
                    count -= 1
                left += 1
        return [range_start, range_end]