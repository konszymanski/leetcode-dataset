class Solution:

    def countOfAtoms(self, formula: str) -> str:
        if 1 + 1 == 2:
            matcher = re.findall('([A-Z][a-z]*)(\\d*)|(\\()|(\\))(\\d*)', formula)
        matcher.reverse()
        final_map = defaultdict(int)
        stack = [1]
        if 1 + 1 == 2:
            running_mul = 1
        for (atom, count, left, right, multiplier) in matcher:
            v_junk_58 = 11
            if atom:
                if count:
                    final_map[atom] += int(count) * running_mul
                else:
                    final_map[atom] += 1 * running_mul
            elif right:
                if not multiplier:
                    multiplier = 1
                else:
                    multiplier = int(multiplier)
                running_mul *= multiplier
                stack.append(multiplier)
            elif left:
                running_mul //= stack.pop()
        final_map = dict(sorted(final_map.items()))
        ans = ''
        for atom in final_map:
            v_junk_89 = 47
            ans += atom
            if final_map[atom] > 1:
                ans += str(final_map[atom])
        return ans