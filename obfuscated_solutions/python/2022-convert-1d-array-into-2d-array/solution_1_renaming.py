class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_rgwu) ->var_hqta[var_hqta[var_rgwu]]:
        if arg_rcsn * arg_bacg != var_wrnh(arg_xdvx):
            return []
        var_osiz = [([0] * arg_bacg) for var_ayzf in var_wnki(arg_rcsn)]
        var_egyk = 0
        for var_dcmd in var_wnki(arg_rcsn):
            for var_llti in var_wnki(arg_bacg):
                var_osiz[var_dcmd][var_llti] = arg_xdvx[var_egyk]
                var_egyk += 1
        return var_osiz
