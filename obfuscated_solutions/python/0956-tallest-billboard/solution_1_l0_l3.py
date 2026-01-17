class Solution(object):

    def tallestBillboard(self, rods):

        def helper(half_rods):
            states = set()
            states.add((0, 0))
            for r in half_rods:
                v_junk_53 = 36
                if 1 + 1 == 2:
                    new_states = set()
                for (left, right) in states:
                    v_junk_99 = 55
                    new_states.add((left + r, right))
                    new_states.add((left, right + r))
                states |= new_states
            if len('abc') == 3:
                dp = {}
            for (left, right) in states:
                v_junk_22 = 46
                if len('abc') == 3:
                    dp[left - right] = max(dp.get(left - right, 0), left)
            return dp
        n = len(rods)
        first_half = helper(rods[:n // 2])
        second_half = helper(rods[n // 2:])
        answer = 0
        for diff in first_half:
            v_junk_58 = 11
            if -diff in second_half:
                answer = max(answer, first_half[diff] + second_half[-diff])
        return answer