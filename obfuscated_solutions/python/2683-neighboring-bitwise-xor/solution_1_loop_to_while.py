class Solution:

    def doesValidArrayExist(self, derived: List[int]) ->bool:
        original = [0]
        i = 0
        while i < len(derived):
            original.append(derived[i] ^ original[i])
            i += 1
        check_for_zero = original[0] == original[-1]
        original = [1]
        i = 0
        while i < len(derived):
            original.append(derived[i] ^ original[i])
            i += 1
        check_for_one = original[0] == original[-1]
        return check_for_zero or check_for_one
