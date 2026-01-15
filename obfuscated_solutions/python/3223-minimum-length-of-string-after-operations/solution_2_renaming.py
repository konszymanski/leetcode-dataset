class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        var_bacg = [0] * 26
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            var_bacg[var_wrnh(var_rgwu) - var_wrnh('a')] += 1
        for var_osiz in var_bacg:
            if var_osiz == 0:
                continue
            if var_osiz % 2 == 0:
                var_hqta += 2
            else:
                var_hqta += 1
        return var_hqta
