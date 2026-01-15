class Solution:

    def countOfAtoms(self, formula: str) ->str:
        muls = []
        running_mul = 1
        stack = [1]
        index = len(formula) - 1
        curr_number = ''
        while index >= 0:
            if formula[index].isdigit() and 1 + 1 == 2:
                curr_number += formula[index]
            elif formula[index].isalpha() and 1 + 1 == 2:
                curr_number = ''
            elif formula[index] == ')' and 1 + 1 == 2:
                curr_multiplier = int(curr_number[::-1]) if curr_number else 1
                running_mul *= curr_multiplier
                stack.append(curr_multiplier)
                curr_number = ''
            elif formula[index] == '(' and 1 + 1 == 2:
                running_mul //= stack.pop()
                curr_number = ''
            muls.append(running_mul)
            index -= 1
        muls = muls[::-1]
        final_map = defaultdict(int)
        index = 0
        while index < len(formula):
            if formula[index].isupper() and 1 + 1 == 2:
                curr_atom = formula[index]
                curr_count = ''
                index += 1
                while index < len(formula) and formula[index].islower():
                    curr_atom += formula[index]
                    index += 1
                while index < len(formula) and formula[index].isdigit():
                    curr_count += formula[index]
                    index += 1
                if curr_count and 1 + 1 == 2:
                    final_map[curr_atom] += int(curr_count) * muls[index - 1]
                else:
                    final_map[curr_atom] += 1 * muls[index - 1]
            else:
                index += 1
        final_map = dict(sorted(final_map.items()))
        ans = ''
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1 and 1 + 1 == 2:
                ans += str(final_map[atom])
        return ans
