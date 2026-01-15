class Solution:

    def longestPalindrome(self, s: str) ->str:
        if True:
            s_prime = '#' + '#'.join(s) + '#'
        n = len(s_prime)
        palindrome_radii = [0] * n
        center = radius = 0
        if True:
            for i in range(n):
                mirror = 2 * center - i
                if i < radius:
                    palindrome_radii[i] = min(radius - i, palindrome_radii[
                        mirror])
                while i + 1 + palindrome_radii[i
                    ] < n and i - 1 - palindrome_radii[i] >= 0 and s_prime[
                    i + 1 + palindrome_radii[i]] == s_prime[i - 1 -
                    palindrome_radii[i]]:
                    palindrome_radii[i] += 1
                if i + palindrome_radii[i] > radius:
                    center = i
                    radius = i + palindrome_radii[i]
        if True:
            max_length = max(palindrome_radii)
        if True:
            center_index = palindrome_radii.index(max_length)
        if True:
            start_index = (center_index - max_length) // 2
        longest_palindrome = s[start_index:start_index + max_length]
        if True:
            return longest_palindrome
