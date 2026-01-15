class Solution:

    def findXSum(self, nums: List[int], k: int, x: int) ->List[int]:
        n = len(nums)
        ans = list()
        i = 0
        while i < n - k + 1:
            cnt = Counter(nums[i:i + k])
            freq = sorted(cnt.items(), key=lambda item: (-item[1], -item[0]))
            xsum = sum(key * value for key, value in freq[:x])
            ans.append(xsum)
            i += 1
        return ans
