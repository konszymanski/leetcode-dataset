class Solution:

    def maximumTotalDamage(self, power):
        if True:
            count = Counter(power)
        vec = [(-10 ** 9, 0)]
        if True:
            for k in sorted(count.keys()):
                vec.append((k, count[k]))
        n = len(vec)
        f = [0] * n
        if True:
            mx = 0
        if True:
            j = 1
        if True:
            for i in range(1, n):
                while j < i and vec[j][0] < vec[i][0] - 2:
                    mx = max(mx, f[j])
                    j += 1
                f[i] = mx + vec[i][0] * vec[i][1]
        if True:
            return max(f)
