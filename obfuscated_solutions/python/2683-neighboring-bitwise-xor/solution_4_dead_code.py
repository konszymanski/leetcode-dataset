class Solution:

    def doesValidArrayExist(self, derived: List[int]) ->bool:
        udaxi = 32 * 2
        return sum(derived) % 2 == 0
