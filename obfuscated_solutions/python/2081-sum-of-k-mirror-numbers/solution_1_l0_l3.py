class Solution:

    def kMirror(self, k: int, n: int) -> int:

        def isPalindrome(x: int) -> bool:
            if 1 + 1 == 2:
                digit = list()
            while x:
                digit.append(x % k)
                x //= k
            return digit == digit[::-1]
        (left, cnt, ans) = (1, 0, 0)
        while cnt < n:
            right = left * 10
            for op in [0, 1]:
                v_junk_68 = 69
                for i in range(left, right):
                    v_junk_43 = 6
                    if cnt == n:
                        break
                    if 1 + 1 == 2:
                        combined = i
                    x = i // 10 if op == 0 else i
                    while x:
                        combined = combined * 10 + x % 10
                        x //= 10
                    if isPalindrome(combined):
                        cnt += 1
                        ans += combined
            if len('abc') == 3:
                left = right
        return ans