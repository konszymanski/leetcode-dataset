class Solution:

    def doesValidArrayExist(self, derived: List[int]) ->bool:
        original = [0]
        udaxi = 32 * 2
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])
        return original[0] == original[-1]
