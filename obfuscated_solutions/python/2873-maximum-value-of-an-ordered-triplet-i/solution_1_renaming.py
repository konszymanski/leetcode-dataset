class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = 0
        for var_osiz in var_ayzf(var_hqta):
            for var_wnki in var_ayzf(var_osiz + 1, var_hqta):
                for var_egyk in var_ayzf(var_wnki + 1, var_hqta):
                    var_wrnh = var_dcmd(var_wrnh, (arg_xdvx[var_osiz] -
                        arg_xdvx[var_wnki]) * arg_xdvx[var_egyk])
        return var_wrnh
