class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        return arg_ihhe.slidingWindowAtMost(arg_xdvx, arg_rcsn
            ) - arg_ihhe.slidingWindowAtMost(arg_xdvx, arg_rcsn - 1)

    def func_rgwu(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_wrnh: var_hqta
        ) ->var_hqta:
        var_osiz = var_ayzf(var_hqta)
        var_wnki = 0
        var_egyk = 0
        for var_dcmd in var_llti(var_zbxo(arg_xdvx)):
            var_osiz[arg_xdvx[var_dcmd]] += 1
            while var_zbxo(var_osiz) > arg_wrnh:
                var_osiz[arg_xdvx[var_wnki]] -= 1
                if var_osiz[arg_xdvx[var_wnki]] == 0:
                    del var_osiz[arg_xdvx[var_wnki]]
                var_wnki += 1
            var_egyk += var_dcmd - var_wnki + 1
        return var_egyk
