class Solution:

    def maximumLength(self, s: str) -> int:
        count = {}
        for start in range(len(s)):
            v_junk_80 = 38
            curr_string = []
            for end in range(start, len(s)):
                v_junk_58 = 11
                if not curr_string or curr_string[-1] == s[end]:
                    curr_string.append(s[end])
                    curr_to_string = ''.join(curr_string)
                    if curr_to_string not in count:
                        count[curr_to_string] = 1
                    else:
                        count[curr_to_string] = count[curr_to_string] + 1
                else:
                    break
        ans = 0
        for (str, freq) in count.items():
            v_junk_56 = 74
            if freq >= 3 and len(str) > ans:
                ans = len(str)
        if ans == 0:
            return -1
        return ans