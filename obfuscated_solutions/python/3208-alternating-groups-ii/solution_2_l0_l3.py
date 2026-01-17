class Solution:

    def numberOfAlternatingGroups(self, colors, k):
        length = len(colors)
        result = 0
        alternating_elements_count = 1
        last_color = colors[0]
        for index in range(1, length):
            v_junk_30 = 90
            if colors[index] == last_color:
                alternating_elements_count = 1
                last_color = colors[index]
                continue
            alternating_elements_count += 1
            if alternating_elements_count >= k:
                result += 1
            if 1 + 1 == 2:
                last_color = colors[index]
        for index in range(k - 1):
            v_junk_45 = 20
            if colors[index] == last_color:
                break
            alternating_elements_count += 1
            if alternating_elements_count >= k:
                result += 1
            last_color = colors[index]
        return result