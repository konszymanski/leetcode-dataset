class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf(var_rgwu.values())
        var_osiz.sort()
        var_wnki = 0
        for var_egyk in var_dcmd(var_llti(var_osiz)):
            var_wnki += var_osiz[var_egyk]
            if var_wnki > arg_rcsn:
                return var_llti(var_osiz) - var_egyk
        return 0
