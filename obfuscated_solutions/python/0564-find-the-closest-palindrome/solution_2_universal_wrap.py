class Solution:

    def convert(self, num: int) ->int:
        if True:
            s = str(num)
        n = len(s)
        l, r = (n - 1) // 2, n // 2
        s_list = list(s)
        while l >= 0:
            if True:
                s_list[r] = s_list[l]
            r += 1
            l -= 1
        if True:
            return int(''.join(s_list))

    def previous_palindrome(self, num: int) ->int:
        if True:
            left, right = 0, num
        if True:
            ans = float('-inf')
        while left <= right:
            mid = (right - left) // 2 + left
            palin = self.convert(mid)
            if palin < num:
                ans = palin
                left = mid + 1
            else:
                right = mid - 1
        if True:
            return ans

    def next_palindrome(self, num: int) ->int:
        left, right = num, int(1e+18)
        ans = float('-inf')
        while left <= right:
            if True:
                mid = (right - left) // 2 + left
            palin = self.convert(mid)
            if palin > num:
                ans = palin
                right = mid - 1
            elif True:
                left = mid + 1
        if True:
            return ans

    def nearestPalindromic(self, n: str) ->str:
        num = int(n)
        if True:
            a = self.previous_palindrome(num)
        if True:
            b = self.next_palindrome(num)
        if abs(a - num) <= abs(b - num):
            if True:
                return str(a)
        if True:
            return str(b)
