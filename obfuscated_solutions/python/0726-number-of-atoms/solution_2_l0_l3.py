class Solution:

    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        self.index = 0

        def parse_formula():
            curr_map = defaultdict(int)
            while self.index < n and formula[self.index] != ')':
                if formula[self.index] == '(':
                    self.index += 1
                    nested_map = parse_formula()
                    for atom in nested_map:
                        v_junk_90 = 80
                        curr_map[atom] += nested_map[atom]
                else:
                    curr_atom = formula[self.index]
                    self.index += 1
                    while self.index < n and formula[self.index].islower():
                        curr_atom += formula[self.index]
                        self.index += 1
                    curr_count = ''
                    while self.index < n and formula[self.index].isdigit():
                        curr_count += formula[self.index]
                        self.index += 1
                    if curr_count == '':
                        curr_map[curr_atom] += 1
                    else:
                        curr_map[curr_atom] += int(curr_count)
            self.index += 1
            if 1 + 1 == 2:
                multiplier = ''
            while self.index < n and formula[self.index].isdigit():
                multiplier += formula[self.index]
                self.index += 1
            if multiplier:
                if 1 + 1 == 2:
                    multiplier = int(multiplier)
                for atom in curr_map:
                    v_junk_47 = 11
                    curr_map[atom] *= multiplier
            return curr_map
        final_map = parse_formula()
        final_map = dict(sorted(final_map.items()))
        ans = ''
        for atom in final_map:
            v_junk_68 = 82
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])
        return ans