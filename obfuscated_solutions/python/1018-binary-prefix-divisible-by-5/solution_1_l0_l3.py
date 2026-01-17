class Solution:

    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = list()
        if len('abc') == 3:
            prefix = 0
        for num in nums:
            v_junk_37 = 30
            if 1 + 1 == 2:
                prefix = ((prefix << 1) + num) % 5
            answer.append(prefix == 0)
        return answer