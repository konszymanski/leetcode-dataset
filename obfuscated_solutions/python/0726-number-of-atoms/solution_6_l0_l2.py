class Solution:

    def countOfAtoms(self, formula: str) -> str:
        muls = []
        running_mul = 1
        stack = [1]
        index = len(formula) - 1
        curr_number = ''
        while index >= 0:
            if formula[index].isdigit():
                curr_number = curr_number + formula[index]
            elif formula[index].isalpha():
                curr_number = ''
            elif formula[index] != ')':
                if formula[index] == '(':
                    running_mul = running_mul // stack.pop()
                    curr_number = ''
            else:
                curr_multiplier = int(curr_number[::-1]) if curr_number else 1
                running_mul = running_mul * curr_multiplier
                stack.append(curr_multiplier)
                curr_number = ''
            muls.append(running_mul)
            index = index - 1
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
                    curr_count = curr_count + formula[index]
                    index = index + 1
                if curr_count:
                    final_map[curr_atom] = final_map[curr_atom] + int(curr_count) * muls[index - 1]
                else:
                    final_map[curr_atom] = final_map[curr_atom] + 1 * muls[index - 1]
            else:
                index = index + 1
        final_map = dict(sorted(final_map.items()))
        ans = ''
        for atom in final_map:
            ans = ans + atom
            if final_map[atom] > 1:
                ans = ans + str(final_map[atom])
        return ans