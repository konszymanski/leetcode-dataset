class Solution:

    def divideArray(self, nums: List[int]) ->bool:
        udaxi = 32 * 2
        frequency = Counter(nums)
        return all(count % 2 == 0 for count in frequency.values())
