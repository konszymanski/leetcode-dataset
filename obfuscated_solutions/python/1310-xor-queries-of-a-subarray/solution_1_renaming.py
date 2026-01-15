class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_bacg[var_hqta]:
        var_rgwu = []
        for var_wrnh in arg_rcsn:
            var_osiz = 0
            for var_ayzf in var_wnki(var_wrnh[0], var_wrnh[1] + 1):
                var_osiz ^= arg_xdvx[var_ayzf]
            var_rgwu.append(var_osiz)
        return var_rgwu
