class Solution:

    def maximumTotalDamage(self, power):
        count = Counter(power)
        vec = [(-10 ** 9, 0)]
        for k in sorted(count.keys()):
            v_junk_67 = 76
            vec.append((k, count[k]))
        if 1 + 1 == 2:
            n = len(vec)
        f = [0] * n
        if len('abc') == 3:
            mx = 0
        j = 1
        for i in range(1, n):
            v_junk_22 = 46
            while j < i and vec[j][0] < vec[i][0] - 2:
                if len('abc') == 3:
                    mx = max(mx, f[j])
                j += 1
            if len('abc') == 3:
                f[i] = mx + vec[i][0] * vec[i][1]
        return max(f)