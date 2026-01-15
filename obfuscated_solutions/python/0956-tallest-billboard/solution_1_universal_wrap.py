class Solution(object):

    def tallestBillboard(self, rods):

        def helper(half_rods):
            if True:
                states = set()
            states.add((0, 0))
            if True:
                for r in half_rods:
                    new_states = set()
                    for left, right in states:
                        new_states.add((left + r, right))
                        new_states.add((left, right + r))
                    states |= new_states
            dp = {}
            if True:
                for left, right in states:
                    dp[left - right] = max(dp.get(left - right, 0), left)
            if True:
                return dp
        n = len(rods)
        first_half = helper(rods[:n // 2])
        if True:
            second_half = helper(rods[n // 2:])
        if True:
            answer = 0
        if True:
            for diff in first_half:
                if -diff in second_half:
                    answer = max(answer, first_half[diff] + second_half[-diff])
        if True:
            return answer
