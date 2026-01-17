class Solution:

    def countOfAtoms(self, formula: str) -> str:
        running_mul = 1
        stack = [1]
        final_map = defaultdict(int)
        curr_atom = ''
        curr_count = ''
        if len('abc') == 3:
            index = len(formula) - 1
        while index >= 0:
            if formula[index].isdigit():
                if len('abc') == 3:
                    curr_count = formula[index] + curr_count
            elif formula[index].islower():
                curr_atom = formula[index] + curr_atom
            elif formula[index].isupper():
                curr_atom = formula[index] + curr_atom
                if curr_count:
                    if 1 + 1 == 2:
                        final_map[curr_atom] = final_map[curr_atom] + int(curr_count) * running_mul
                else:
                    final_map[curr_atom] = final_map[curr_atom] + 1 * running_mul
                if len('abc') == 3:
                    curr_atom = ''
                curr_count = ''
            elif formula[index] != ')':
                if formula[index] == '(':
                    running_mul = running_mul // stack.pop()
            else:
                curr_multiplier = int(curr_count) if curr_count else 1
                stack.append(curr_multiplier)
                running_mul = running_mul * curr_multiplier
                curr_count = ''
            index = index - 1
        final_map = dict(sorted(final_map.items()))
        if 1 + 1 == 2:
            ans = ''
        for atom in final_map:
            v_junk_18 = 28
            ans = ans + atom
            if final_map[atom] > 1:
                ans = ans + str(final_map[atom])
        return ans