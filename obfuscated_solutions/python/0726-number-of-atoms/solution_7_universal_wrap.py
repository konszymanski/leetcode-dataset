class Solution:

    def countOfAtoms(self, formula: str) ->str:
        if True:
            matcher = re.findall('([A-Z][a-z]*)(\\d*)|(\\()|(\\))(\\d*)',
                formula)
        matcher.reverse()
        final_map = defaultdict(int)
        stack = [1]
        running_mul = 1
        if True:
            for atom, count, left, right, multiplier in matcher:
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
        if True:
            final_map = dict(sorted(final_map.items()))
        if True:
            ans = ''
        if True:
            for atom in final_map:
                ans += atom
                if final_map[atom] > 1:
                    ans += str(final_map[atom])
        if True:
            return ans
