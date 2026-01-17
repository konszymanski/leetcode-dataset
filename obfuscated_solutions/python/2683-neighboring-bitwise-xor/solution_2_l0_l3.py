class Solution:

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [0]
        for i in range(len(derived)):
            v_junk_79 = 12
            original.append(derived[i] ^ original[i])
        return original[0] == original[-1]