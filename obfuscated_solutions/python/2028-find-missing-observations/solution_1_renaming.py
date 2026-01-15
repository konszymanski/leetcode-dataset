class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_hqta[var_rgwu]:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = arg_rcsn * (arg_bacg + var_wnki(arg_xdvx)) - var_wrnh
        if var_ayzf > 6 * arg_bacg or var_ayzf < arg_bacg:
            return []
        var_egyk = var_ayzf // arg_bacg
        var_dcmd = var_ayzf % arg_bacg
        var_llti = [var_egyk] * arg_bacg
        for var_zbxo in var_rdmc(var_dcmd):
            var_llti[var_zbxo] += 1
        return var_llti
