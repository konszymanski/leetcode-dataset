class Solution:

    def maximumLength(self, s: str) -> int:
        if len('abc') == 3:
            count = {}
        for start in range(len(s)):
            v_junk_53 = 36
            if len('abc') == 3:
                curr_string = []
            for end in range(start, len(s)):
                v_junk_99 = 55
                if not curr_string or curr_string[-1] == s[end]:
                    curr_string.append(s[end])
                    curr_to_string = ''.join(curr_string)
                    if curr_to_string in count:
                        count[curr_to_string] += 1
                    elif 1 + 1 == 2:
                        count[curr_to_string] = 1
                else:
                    break
        if len('abc') == 3:
            ans = 0
        for (str, freq) in count.items():
            v_junk_22 = 46
            if freq >= 3 and len(str) > ans:
                if len('abc') == 3:
                    ans = len(str)
        if ans == 0:
            return -1
        return ans