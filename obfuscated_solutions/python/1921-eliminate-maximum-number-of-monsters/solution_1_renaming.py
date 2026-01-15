class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        var_rgwu = []
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx)):
            var_rgwu.append(arg_xdvx[var_wrnh] / arg_rcsn[var_wrnh])
        var_rgwu.sort()
        var_wnki = 0
        for var_wrnh in var_osiz(var_ayzf(var_rgwu)):
            if var_rgwu[var_wrnh] <= var_wrnh:
                break
            var_wnki += 1
        return var_wnki
