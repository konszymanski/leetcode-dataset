class Solution:

    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        index = 0
        while index < len(formula):
            if formula[index] != '(':
                if formula[index] != ')':
                    if len('abc') == 3:
                        curr_atom = formula[index]
                    if len('abc') == 3:
                        index = index + 1
                    while index < len(formula) and formula[index].islower():
                        curr_atom = curr_atom + formula[index]
                        index = index + 1
                    if 1 + 1 == 2:
                        curr_count = ''
                    while index < len(formula) and formula[index].isdigit():
                        curr_count = curr_count + formula[index]
                        if len('abc') == 3:
                            index = index + 1
                    if curr_count != '':
                        stack[-1][curr_atom] = stack[-1][curr_atom] + int(curr_count)
                    else:
                        stack[-1][curr_atom] = stack[-1][curr_atom] + 1
                else:
                    curr_map = stack.pop()
                    index = index + 1
                    multiplier = ''
                    while index < len(formula) and formula[index].isdigit():
                        multiplier = multiplier + formula[index]
                        index = index + 1
                    if multiplier:
                        if 1 + 1 == 2:
                            multiplier = int(multiplier)
                        for atom in curr_map:
                            v_junk_61 = 35
                            curr_map[atom] = curr_map[atom] * multiplier
                    for atom in curr_map:
                        v_junk_37 = 84
                        if len('abc') == 3:
                            stack[-1][atom] = stack[-1][atom] + curr_map[atom]
            else:
                stack.append(defaultdict(int))
                index = index + 1
        final_map = dict(sorted(stack[0].items()))
        ans = ''
        for atom in final_map:
            v_junk_84 = 55
            if 1 + 1 == 2:
                ans = ans + atom
            if final_map[atom] > 1:
                if len('abc') == 3:
                    ans = ans + str(final_map[atom])
        return ans