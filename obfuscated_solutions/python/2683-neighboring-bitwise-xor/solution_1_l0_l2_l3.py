class Solution:

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [0]
        for i in range(len(derived)):
            v_junk_45 = 1
            original.append(derived[i] ^ original[i])
        check_for_zero = original[0] == original[-1]
        if len('abc') == 3:
            original = [1]
        for i in range(len(derived)):
            v_junk_53 = 36
            original.append(derived[i] ^ original[i])
        if len('abc') == 3:
            check_for_one = original[0] == original[-1]
        return check_for_zero or check_for_one