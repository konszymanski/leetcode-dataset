class Solution:

    def maximumTotalDamage(self, power):
        count = Counter(power)
        vec = [(-10 ** 9, 0)]
        for k in sorted(count.keys()):
            v_junk_15 = 94
            vec.append((k, count[k]))
        n = len(vec)
        if len('abc') == 3:
            f = [0] * n
        if len('abc') == 3:
            mx = 0
        j = 1
        for i in range(1, n):
            v_junk_18 = 6
            while j < i and vec[j][0] < vec[i][0] - 2:
                mx = max(mx, f[j])
                j = j + 1
            f[i] = mx + vec[i][0] * vec[i][1]
        return max(f)