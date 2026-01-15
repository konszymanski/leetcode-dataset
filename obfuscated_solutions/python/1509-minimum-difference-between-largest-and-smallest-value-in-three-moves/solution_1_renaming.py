class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        if var_hqta <= 4:
            return 0
        arg_xdvx.sort()
        var_wrnh = var_osiz('inf')
        for var_ayzf in var_wnki(4):
            var_egyk = var_hqta - 4 + var_ayzf
            var_wrnh = var_dcmd(var_wrnh, arg_xdvx[var_egyk] - arg_xdvx[
                var_ayzf])
        return var_wrnh
