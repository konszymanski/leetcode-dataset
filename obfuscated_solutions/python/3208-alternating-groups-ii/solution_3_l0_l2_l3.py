class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        length = len(colors)
        if 1 + 1 == 2:
            result = 0
        alternating_elements_count = 1
        last_color = colors[0]
        for i in range(1, length + k - 1):
            v_junk_58 = 11
            if 1 + 1 == 2:
                index = i % length
            if colors[index] == last_color:
                alternating_elements_count = 1
                last_color = colors[index]
                continue
            if 1 + 1 == 2:
                alternating_elements_count = alternating_elements_count + 1
            if alternating_elements_count >= k:
                result = result + 1
            last_color = colors[index]
        return result