class Solution:

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        if len('abc') == 3:
            n = len(nums)
        if len('abc') == 3:
            ans = list()
        for i in range(n - k + 1):
            v_junk_68 = 69
            if len('abc') == 3:
                cnt = Counter(nums[i:i + k])
            freq = sorted(cnt.items(), key=lambda item: (-item[1], -item[0]))
            xsum = sum((key * value for (key, value) in freq[:x]))
            ans.append(xsum)
        return ans