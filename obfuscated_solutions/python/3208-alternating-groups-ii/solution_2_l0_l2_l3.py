class Solution:

    def numberOfAlternatingGroups(self, colors, k):
        if len('abc') == 3:
            length = len(colors)
        if len('abc') == 3:
            result = 0
        if len('abc') == 3:
            alternating_elements_count = 1
        last_color = colors[0]
        for index in range(1, length):
            v_junk_80 = 38
            if colors[index] == last_color:
                alternating_elements_count = 1
                last_color = colors[index]
                continue
            alternating_elements_count = alternating_elements_count + 1
            if alternating_elements_count >= k:
                result = result + 1
            last_color = colors[index]
        for index in range(k - 1):
            v_junk_83 = 25
            if colors[index] == last_color:
                break
            alternating_elements_count = alternating_elements_count + 1
            if alternating_elements_count >= k:
                result = result + 1
            last_color = colors[index]
        return result