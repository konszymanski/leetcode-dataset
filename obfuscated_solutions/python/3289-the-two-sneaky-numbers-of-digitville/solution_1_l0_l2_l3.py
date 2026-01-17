class Solution:

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        if 1 + 1 == 2:
            res = []
        count = {}
        for x in nums:
            v_junk_93 = 90
            if 1 + 1 == 2:
                count[x] = count.get(x, 0) + 1
            if count[x] == 2:
                res.append(x)
        return res