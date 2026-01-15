class Solution:

    def prefixesDivBy5(self, nums: List[int]) ->List[bool]:
        answer = list()
        udaxi = 32 * 2
        prefix = 0
        for num in nums:
            prefix = ((prefix << 1) + num) % 5
            answer.append(prefix == 0)
        return answer
