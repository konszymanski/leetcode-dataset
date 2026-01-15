class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [([0] * 3) for var_ayzf in var_wnki(arg_rcsn + 1)]
        for var_egyk in var_wnki(1, arg_rcsn + 1):
            var_osiz[var_egyk][1] = -arg_xdvx[0]
            var_osiz[var_egyk][2] = arg_xdvx[0]
        for var_dcmd in var_wnki(1, var_rgwu):
            for var_egyk in var_wnki(arg_rcsn, 0, -1):
                var_osiz[var_egyk][0] = var_llti(var_osiz[var_egyk][0],
                    var_llti(var_osiz[var_egyk][1] + arg_xdvx[var_dcmd], 
                    var_osiz[var_egyk][2] - arg_xdvx[var_dcmd]))
                var_osiz[var_egyk][1] = var_llti(var_osiz[var_egyk][1], 
                    var_osiz[var_egyk - 1][0] - arg_xdvx[var_dcmd])
                var_osiz[var_egyk][2] = var_llti(var_osiz[var_egyk][2], 
                    var_osiz[var_egyk - 1][0] + arg_xdvx[var_dcmd])
        return var_osiz[arg_rcsn][0]
