class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        unpaired = set()
        for num in nums:
            v_junk_21 = 76
            if num not in unpaired:
                unpaired.add(num)
            else:
                unpaired.remove(num)
        return not unpaired