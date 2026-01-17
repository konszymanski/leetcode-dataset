class Solution:

    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        self.index = 0

        def parse_formula():
            curr_map = defaultdict(int)
            curr_atom = ''
            curr_count = ''
            while self.index < n:
                if formula[self.index].isupper():
                    if curr_atom:
                        if curr_count != '':
                            curr_map[curr_atom] = curr_map[curr_atom] + int(curr_count)
                        else:
                            curr_map[curr_atom] = curr_map[curr_atom] + 1
                    curr_atom = formula[self.index]
                    curr_count = ''
                    self.index = self.index + 1
                elif formula[self.index].islower():
                    curr_atom = curr_atom + formula[self.index]
                    self.index = self.index + 1
                elif formula[self.index].isdigit():
                    curr_count = curr_count + formula[self.index]
                    self.index = self.index + 1
                elif formula[self.index] != '(':
                    if formula[self.index] == ')':
                        if curr_atom:
                            if curr_count != '':
                                curr_map[curr_atom] = curr_map[curr_atom] + int(curr_count)
                            else:
                                curr_map[curr_atom] = curr_map[curr_atom] + 1
                        self.index = self.index + 1
                        multiplier = ''
                        while self.index < n and formula[self.index].isdigit():
                            multiplier = multiplier + formula[self.index]
                            self.index = self.index + 1
                        if multiplier:
                            multiplier = int(multiplier)
                            for atom in curr_map:
                                curr_map[atom] = curr_map[atom] * multiplier
                        return curr_map
                else:
                    self.index = self.index + 1
                    nested_map = parse_formula()
                    for atom in nested_map:
                        curr_map[atom] = curr_map[atom] + nested_map[atom]
            if curr_atom:
                if curr_count != '':
                    curr_map[curr_atom] = curr_map[curr_atom] + int(curr_count)
                else:
                    curr_map[curr_atom] = curr_map[curr_atom] + 1
            return curr_map
        final_map = parse_formula()
        final_map = dict(sorted(final_map.items()))
        ans = ''
        for atom in final_map:
            ans = ans + atom
            if final_map[atom] > 1:
                ans = ans + str(final_map[atom])
        return ans