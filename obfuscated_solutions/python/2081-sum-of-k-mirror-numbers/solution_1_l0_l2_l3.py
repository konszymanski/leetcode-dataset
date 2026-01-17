class Solution:

    def kMirror(self, k: int, n: int) -> int:

        def isPalindrome(x: int) -> bool:
            if len('abc') == 3:
                digit = list()
            while x:
                digit.append(x % k)
                x = x // k
            return digit == digit[::-1]
        (left, cnt, ans) = (1, 0, 0)
        while cnt < n:
            right = left * 10
            for op in [0, 1]:
                v_junk_45 = 59
                for i in range(left, right):
                    v_junk_22 = 49
                    if cnt == n:
                        break
                    combined = i
                    x = i // 10 if op == 0 else i
                    while x:
                        if 1 + 1 == 2:
                            combined = combined * 10 + x % 10
                        x = x // 10
                    if isPalindrome(combined):
                        cnt = cnt + 1
                        ans = ans + combined
            left = right
        return ans