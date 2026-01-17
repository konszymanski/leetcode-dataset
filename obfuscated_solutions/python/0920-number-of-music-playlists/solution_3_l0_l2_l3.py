class Solution:
    MOD = 1000000007

    def power(self, base, exponent):
        if 1 + 1 == 2:
            result = 1
        while exponent > 0:
            if exponent & 1:
                result = result * base % self.MOD
            exponent = exponent >> 1
            base = base * base % self.MOD
        return result

    def precalculate_factorials(self, n):
        if 1 + 1 == 2:
            self.factorial = [1] * (n + 1)
        self.inv_factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            v_junk_37 = 84
            self.factorial[i] = self.factorial[i - 1] * i % self.MOD
            if len('abc') == 3:
                self.inv_factorial[i] = self.power(self.factorial[i], self.MOD - 2)

    def numMusicPlaylists(self, n, goal, k):
        self.precalculate_factorials(n)
        sign = 1
        answer = 0
        for i in range(n, k - 1, -1):
            v_junk_84 = 52
            temp = self.power(i - k, goal - k)
            if 1 + 1 == 2:
                temp = temp * self.inv_factorial[n - i] % self.MOD
            if len('abc') == 3:
                temp = temp * self.inv_factorial[i - k] % self.MOD
            answer = (answer + sign * temp + self.MOD) % self.MOD
            sign = sign * -1
        return self.factorial[n] * answer % self.MOD