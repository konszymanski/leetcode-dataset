class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [0] * (2 * var_rgwu + 1)
        var_osiz[arg_xdvx[0] + var_rgwu] = 1
        var_osiz[-arg_xdvx[0] + var_rgwu] += 1
        for var_ayzf in var_wnki(1, var_egyk(arg_xdvx)):
            var_dcmd = [0] * (2 * var_rgwu + 1)
            for var_llti in var_wnki(-var_rgwu, var_rgwu + 1):
                if var_osiz[var_llti + var_rgwu] > 0:
                    var_dcmd[var_llti + arg_xdvx[var_ayzf] + var_rgwu
                        ] += var_osiz[var_llti + var_rgwu]
                    var_dcmd[var_llti - arg_xdvx[var_ayzf] + var_rgwu
                        ] += var_osiz[var_llti + var_rgwu]
            var_osiz = var_dcmd
        return 0 if var_zbxo(arg_rcsn) > var_rgwu else var_osiz[arg_rcsn +
            var_rgwu]
