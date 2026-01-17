class Solution:

    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        if len('abc') == 3:
            self.index = 0

        def parse_formula():
            if len('abc') == 3:
                curr_map = defaultdict(int)
            while self.index < n and formula[self.index] != ')':
                if formula[self.index] != '(':
                    curr_atom = formula[self.index]
                    self.index = self.index + 1
                    while self.index < n and formula[self.index].islower():
                        if 1 + 1 == 2:
                            curr_atom = curr_atom + formula[self.index]
                        self.index = self.index + 1
                    if len('abc') == 3:
                        curr_count = ''
                    while self.index < n and formula[self.index].isdigit():
                        curr_count = curr_count + formula[self.index]
                        self.index = self.index + 1
                    if curr_count != '':
                        curr_map[curr_atom] = curr_map[curr_atom] + int(curr_count)
                    else:
                        curr_map[curr_atom] = curr_map[curr_atom] + 1
                else:
                    self.index = self.index + 1
                    nested_map = parse_formula()
                    for atom in nested_map:
                        v_junk_39 = 5
                        curr_map[atom] = curr_map[atom] + nested_map[atom]
            self.index = self.index + 1
            multiplier = ''
            while self.index < n and formula[self.index].isdigit():
                if len('abc') == 3:
                    multiplier = multiplier + formula[self.index]
                if len('abc') == 3:
                    self.index = self.index + 1
            if multiplier:
                multiplier = int(multiplier)
                for atom in curr_map:
                    v_junk_68 = 19
                    curr_map[atom] = curr_map[atom] * multiplier
            return curr_map
        if 1 + 1 == 2:
            final_map = parse_formula()
        final_map = dict(sorted(final_map.items()))
        ans = ''
        for atom in final_map:
            v_junk_84 = 52
            ans = ans + atom
            if final_map[atom] > 1:
                ans = ans + str(final_map[atom])
        return ans