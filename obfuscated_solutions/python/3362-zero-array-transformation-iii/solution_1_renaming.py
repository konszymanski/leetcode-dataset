class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn:
        var_bacg[var_bacg[var_hqta]]) ->var_hqta:
        arg_rcsn.sort(key=lambda x: var_rgwu[0])
        var_wrnh = []
        var_osiz = [0] * (var_ayzf(arg_xdvx) + 1)
        var_wnki = 0
        var_egyk = 0
        for var_dcmd, var_llti in var_zbxo(arg_xdvx):
            var_wnki += var_osiz[var_dcmd]
            while var_egyk < var_ayzf(arg_rcsn) and arg_rcsn[var_egyk][0
                ] == var_dcmd:
                var_rdmc(var_wrnh, -arg_rcsn[var_egyk][1])
                var_egyk += 1
            while var_wnki < var_llti and var_wrnh and -var_wrnh[0
                ] >= var_dcmd:
                var_wnki += 1
                var_osiz[-var_rjut(var_wrnh) + 1] -= 1
            if var_wnki < var_llti:
                return -1
        return var_ayzf(var_wrnh)
