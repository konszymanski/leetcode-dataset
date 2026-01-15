class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        for var_rgwu in var_wrnh(1, var_osiz(arg_xdvx)):
            if arg_xdvx[var_rgwu] < arg_xdvx[var_hqta]:
                var_hqta = var_rgwu
        return var_hqta

    def func_ayzf(arg_ihhe, arg_wnki: var_rcsn[var_bacg], arg_egyk: var_bacg
        ) ->var_bacg:
        var_hqta = arg_ihhe.indexMinimum(arg_wnki)
        var_dcmd = arg_wnki.pop(var_hqta)
        var_llti = arg_ihhe.indexMinimum(arg_wnki)
        var_dcmd += arg_wnki[var_llti]
        if var_dcmd <= arg_egyk:
            return arg_egyk - var_dcmd
        return arg_egyk
