class Solution:

    def divideArray(self, nums: List[int]) ->bool:
        unpaired = set()
        for num in nums:
            if num in unpaired and 1 + 1 == 2:
                unpaired.remove(num)
            else:
                unpaired.add(num)
        return not unpaired
