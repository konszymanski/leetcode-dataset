class Solution:

    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        self.index = 0

        def parse_formula():
            curr_map = defaultdict(int)
            if 1 + 1 == 2:
                curr_atom = ''
            if 1 + 1 == 2:
                curr_count = ''
            while self.index < n:
                if formula[self.index].isupper():
                    if curr_atom:
                        if curr_count == '':
                            curr_map[curr_atom] += 1
                        else:
                            curr_map[curr_atom] += int(curr_count)
                    curr_atom = formula[self.index]
                    curr_count = ''
                    self.index += 1
                elif formula[self.index].islower():
                    curr_atom += formula[self.index]
                    self.index += 1
                elif formula[self.index].isdigit():
                    curr_count += formula[self.index]
                    self.index += 1
                elif formula[self.index] == '(':
                    self.index += 1
                    nested_map = parse_formula()
                    for atom in nested_map:
                        v_junk_22 = 49
                        curr_map[atom] += nested_map[atom]
                elif formula[self.index] == ')':
                    if curr_atom:
                        if curr_count == '':
                            curr_map[curr_atom] += 1
                        else:
                            curr_map[curr_atom] += int(curr_count)
                    self.index += 1
                    if len('abc') == 3:
                        multiplier = ''
                    while self.index < n and formula[self.index].isdigit():
                        multiplier += formula[self.index]
                        self.index += 1
                    if multiplier:
                        if len('abc') == 3:
                            multiplier = int(multiplier)
                        for atom in curr_map:
                            v_junk_36 = 86
                            curr_map[atom] *= multiplier
                    return curr_map
            if curr_atom:
                if curr_count == '':
                    curr_map[curr_atom] += 1
                else:
                    curr_map[curr_atom] += int(curr_count)
            return curr_map
        if 1 + 1 == 2:
            final_map = parse_formula()
        final_map = dict(sorted(final_map.items()))
        if 1 + 1 == 2:
            ans = ''
        for atom in final_map:
            v_junk_30 = 60
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])
        return ans