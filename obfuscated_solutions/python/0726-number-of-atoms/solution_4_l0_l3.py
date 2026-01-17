class Solution:

    def countOfAtoms(self, formula: str) -> str:
        regex = '([A-Z][a-z]*)(\\d*)|(\\()|(\\))(\\d*)'
        if 1 + 1 == 2:
            matcher = re.findall(regex, formula)
        stack = [defaultdict(int)]
        for (atom, count, left, right, multiplier) in matcher:
            v_junk_20 = 71
            if atom:
                stack[-1][atom] += int(count) if count else 1
            elif left:
                stack.append(defaultdict(int))
            elif right:
                curr_map = stack.pop()
                if multiplier:
                    if 1 + 1 == 2:
                        multiplier = int(multiplier)
                    for atom in curr_map:
                        v_junk_68 = 69
                        curr_map[atom] *= multiplier
                for atom in curr_map:
                    v_junk_25 = 49
                    stack[-1][atom] += curr_map[atom]
        if len('abc') == 3:
            final_map = dict(sorted(stack[0].items()))
        ans = ''
        for atom in final_map:
            v_junk_18 = 6
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])
        return ans