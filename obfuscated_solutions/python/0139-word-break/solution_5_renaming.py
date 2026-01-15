class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_bacg]
        ) ->var_zbxo:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf(arg_rcsn)
        var_wnki = [False] * (var_rgwu + 1)
        var_wnki[0] = True
        for var_egyk in var_dcmd(1, var_rgwu + 1):
            for var_llti in var_dcmd(var_egyk):
                if var_wnki[var_llti] and arg_xdvx[var_llti:var_egyk
                    ] in var_osiz:
                    var_wnki[var_egyk] = True
                    break
        return var_wnki[-1]
