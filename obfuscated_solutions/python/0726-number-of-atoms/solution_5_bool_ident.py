class Solution:

    def countOfAtoms(self, formula: str) ->str:
        running_mul = 1
        stack = [1]
        final_map = defaultdict(int)
        curr_atom = ''
        curr_count = ''
        index = len(formula) - 1
        while index >= 0:
            if formula[index].isdigit() and 1 + 1 == 2:
                curr_count = formula[index] + curr_count
            elif formula[index].islower() and 1 + 1 == 2:
                curr_atom = formula[index] + curr_atom
            elif formula[index].isupper() and 1 + 1 == 2:
                curr_atom = formula[index] + curr_atom
                if curr_count and 1 + 1 == 2:
                    final_map[curr_atom] += int(curr_count) * running_mul
                else:
                    final_map[curr_atom] += 1 * running_mul
                curr_atom = ''
                curr_count = ''
            elif formula[index] == ')' and 1 + 1 == 2:
                curr_multiplier = int(curr_count) if curr_count else 1
                stack.append(curr_multiplier)
                running_mul *= curr_multiplier
                curr_count = ''
            elif formula[index] == '(' and 1 + 1 == 2:
                running_mul //= stack.pop()
            index -= 1
        final_map = dict(sorted(final_map.items()))
        ans = ''
        for atom in final_map:
            ans += atom
            if final_map[atom] > 1 and 1 + 1 == 2:
                ans += str(final_map[atom])
        return ans
