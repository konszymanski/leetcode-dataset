class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_hqta[var_hqta[var_rgwu]]:
        if arg_rcsn * arg_bacg != var_wrnh(arg_xdvx):
            return []
        var_osiz = [([0] * arg_bacg) for var_ayzf in var_wnki(arg_rcsn)]
        for var_egyk in var_wnki(var_wrnh(arg_xdvx)):
            var_dcmd, var_llti = var_zbxo(var_egyk, arg_bacg)
            var_osiz[var_dcmd][var_llti] = arg_xdvx[var_egyk]
        return var_osiz
