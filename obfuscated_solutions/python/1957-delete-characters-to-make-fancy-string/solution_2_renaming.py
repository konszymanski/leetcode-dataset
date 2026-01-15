class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        if var_bacg(arg_xdvx) < 3:
            return arg_xdvx
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 2
        for var_osiz in var_ayzf(2, var_bacg(arg_xdvx)):
            if var_hqta[var_osiz] != var_hqta[var_wrnh - 1] or var_hqta[
                var_osiz] != var_hqta[var_wrnh - 2]:
                var_hqta[var_wrnh] = var_hqta[var_osiz]
                var_wrnh += 1
        return ''.join(var_hqta[:var_wrnh])
