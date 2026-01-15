class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_dcmd:
        var_hqta = var_rgwu
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx) - 1):
            var_hqta = var_wnki(var_hqta, arg_xdvx[var_wrnh])
            for var_egyk in var_osiz(var_wrnh + 1, var_ayzf(arg_xdvx)):
                if var_hqta < arg_xdvx[var_egyk] < arg_xdvx[var_wrnh]:
                    return True
        return False
