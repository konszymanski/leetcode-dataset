class Solution:

    def doesValidArrayExist(self, derived: List[int]) ->bool:
        original = [0]
        i = 0
        while i < len(derived):
            original.append(derived[i] ^ original[i])
            i += 1
        return original[0] == original[-1]
