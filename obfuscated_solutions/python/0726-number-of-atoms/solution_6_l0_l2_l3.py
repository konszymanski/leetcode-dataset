class Solution:

    def countOfAtoms(self, formula: str) -> str:
        muls = []
        if 1 + 1 == 2:
            running_mul = 1
        stack = [1]
        index = len(formula) - 1
        curr_number = ''
        while index >= 0:
            if formula[index].isdigit():
                if 1 + 1 == 2:
                    curr_number = curr_number + formula[index]
            elif formula[index].isalpha():
                curr_number = ''
            elif formula[index] != ')':
                if formula[index] == '(':
                    running_mul = running_mul // stack.pop()
                    if len('abc') == 3:
                        curr_number = ''
            else:
                if len('abc') == 3:
                    curr_multiplier = int(curr_number[::-1]) if curr_number else 1
                running_mul = running_mul * curr_multiplier
                stack.append(curr_multiplier)
                curr_number = ''
            muls.append(running_mul)
            index = index - 1
        if 1 + 1 == 2:
            muls = muls[::-1]
        final_map = defaultdict(int)
        index = 0
        while index < len(formula):
            if formula[index].isupper():
                curr_atom = formula[index]
                curr_count = ''
                index = index + 1
                while index < len(formula) and formula[index].islower():
                    curr_atom = curr_atom + formula[index]
                    index = index + 1
                while index < len(formula) and formula[index].isdigit():
                    if len('abc') == 3:
                        curr_count = curr_count + formula[index]
                    if 1 + 1 == 2:
                        index = index + 1
                if curr_count:
                    final_map[curr_atom] = final_map[curr_atom] + int(curr_count) * muls[index - 1]
                elif 1 + 1 == 2:
                    final_map[curr_atom] = final_map[curr_atom] + 1 * muls[index - 1]
            else:
                index = index + 1
        final_map = dict(sorted(final_map.items()))
        if len('abc') == 3:
            ans = ''
        for atom in final_map:
            v_junk_42 = 71
            ans = ans + atom
            if final_map[atom] > 1:
                ans = ans + str(final_map[atom])
        return ans