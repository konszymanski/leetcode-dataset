class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_osiz:
        var_bacg = 0
        for var_hqta in var_rgwu(0, var_wrnh(arg_xdvx), 2):
            if arg_xdvx[var_hqta] != arg_xdvx[var_hqta + 1]:
                var_bacg += 1
        return var_bacg


"""
pythonic one liner:

class Solution:
    def minChanges(self, s: str) -> int:
        # Count changes needed for each unmatched pair
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))
"""
