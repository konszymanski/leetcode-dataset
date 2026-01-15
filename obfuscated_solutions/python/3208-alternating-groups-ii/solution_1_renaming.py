class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        for var_rgwu in var_wrnh(arg_rcsn - 1):
            arg_xdvx.append(arg_xdvx[var_rgwu])
        var_osiz = var_ayzf(arg_xdvx)
        var_wnki = 0
        var_egyk = 0
        var_dcmd = 1
        while var_dcmd < var_osiz:
            if arg_xdvx[var_dcmd] == arg_xdvx[var_dcmd - 1]:
                var_egyk = var_dcmd
                var_dcmd += 1
                continue
            var_dcmd += 1
            if var_dcmd - var_egyk < arg_rcsn:
                continue
            var_wnki += 1
            var_egyk += 1
        return var_wnki
