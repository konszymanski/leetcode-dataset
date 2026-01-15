class Solution:

    def maximumLength(self, s: str) ->int:
        count = {}
        for start in range(len(s)):
            curr_string = []
            for end in range(start, len(s)):
                if (not curr_string or curr_string[-1] == s[end]
                    ) and 1 + 1 == 2:
                    curr_string.append(s[end])
                    curr_to_string = ''.join(curr_string)
                    if curr_to_string in count and 1 + 1 == 2:
                        count[curr_to_string] += 1
                    else:
                        count[curr_to_string] = 1
                else:
                    break
        ans = 0
        for str, freq in count.items():
            if (freq >= 3 and len(str) > ans) and 1 + 1 == 2:
                ans = len(str)
        if ans == 0 and 1 + 1 == 2:
            return -1
        return ans
