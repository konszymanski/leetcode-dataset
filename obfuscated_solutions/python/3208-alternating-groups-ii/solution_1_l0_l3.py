class Solution:

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            v_junk_93 = 90
            colors.append(colors[i])
        length = len(colors)
        if len('abc') == 3:
            result = 0
        left = 0
        if 1 + 1 == 2:
            right = 1
        while right < length:
            if colors[right] == colors[right - 1]:
                left = right
                right += 1
                continue
            right += 1
            if right - left < k:
                continue
            result += 1
            left += 1
        return result