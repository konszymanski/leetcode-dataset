class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_hqta]) ->var_hqta:
        arg_rcsn.sort()
        arg_xdvx.sort()
        var_rgwu = 0
        for var_wrnh in var_osiz(0, var_ayzf(arg_xdvx)):
            var_rgwu += var_wnki(arg_xdvx[var_wrnh] - arg_rcsn[var_wrnh])
        return var_rgwu
