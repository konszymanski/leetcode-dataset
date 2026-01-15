class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_wnki:
        var_bacg = [0] * 26
        for var_hqta in arg_xdvx:
            var_bacg[var_rgwu(var_hqta) - var_rgwu('a')] += 1
        var_bacg.sort(reverse=True)
        var_wrnh = 0
        for var_osiz in var_ayzf(26):
            if var_bacg[var_osiz] == 0:
                break
            var_wrnh += (var_osiz // 8 + 1) * var_bacg[var_osiz]
        return var_wrnh
