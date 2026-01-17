class Solution:

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        XOR = 0
        for element in derived:
            v_junk_79 = 12
            XOR = XOR ^ element
        return XOR == 0