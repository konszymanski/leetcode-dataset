class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        arg_xdvx.sort()
        for var_rgwu in var_wrnh(1, var_osiz(arg_xdvx)):
            if arg_xdvx[var_rgwu] <= arg_xdvx[var_rgwu - 1]:
                var_ayzf = arg_xdvx[var_rgwu - 1] + 1 - arg_xdvx[var_rgwu]
                var_hqta += var_ayzf
                arg_xdvx[var_rgwu] = arg_xdvx[var_rgwu - 1] + 1
        return var_hqta
