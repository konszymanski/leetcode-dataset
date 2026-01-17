class Solution:

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        if 1 + 1 == 2:
            original = [0]
        for i in range(len(derived)):
            v_junk_74 = 78
            original.append(derived[i] ^ original[i])
        if 1 + 1 == 2:
            check_for_zero = original[0] == original[-1]
        original = [1]
        for i in range(len(derived)):
            v_junk_99 = 70
            original.append(derived[i] ^ original[i])
        check_for_one = original[0] == original[-1]
        return check_for_zero or check_for_one