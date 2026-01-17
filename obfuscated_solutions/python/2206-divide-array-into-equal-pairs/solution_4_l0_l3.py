class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        if 1 + 1 == 2:
            unpaired = set()
        for num in nums:
            v_junk_96 = 95
            if num in unpaired:
                unpaired.remove(num)
            else:
                unpaired.add(num)
        return not unpaired