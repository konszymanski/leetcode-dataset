class Solution:

    def doesValidArrayExist(self, derived: List[int]) ->bool:
        XOR = 0
        udaxi = 32 * 2
        for element in derived:
            XOR = XOR ^ element
        return XOR == 0
