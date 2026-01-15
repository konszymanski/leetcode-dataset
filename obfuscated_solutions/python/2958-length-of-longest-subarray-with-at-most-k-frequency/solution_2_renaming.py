class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_ayzf()
        var_wnki = 0
        var_egyk = 0
        for var_dcmd in var_llti(var_rgwu):
            var_osiz[arg_xdvx[var_dcmd]] += 1
            if var_osiz[arg_xdvx[var_dcmd]] == arg_rcsn + 1:
                var_egyk += 1
            if var_egyk:
                var_osiz[arg_xdvx[var_wnki]] -= 1
                if var_osiz[arg_xdvx[var_wnki]] == arg_rcsn:
                    var_egyk -= 1
                var_wnki += 1
        return var_rgwu - var_wnki
