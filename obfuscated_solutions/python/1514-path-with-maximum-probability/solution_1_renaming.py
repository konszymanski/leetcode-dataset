class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh, arg_rcsn: var_osiz[var_osiz
        [var_wrnh]], arg_bacg: var_osiz[var_ayzf], arg_hqta: var_wrnh,
        arg_rgwu: var_wrnh) ->var_ayzf:
        var_wnki = [0] * arg_xdvx
        var_wnki[arg_hqta] = 1
        for var_egyk in var_dcmd(arg_xdvx - 1):
            var_llti = 0
            for var_zbxo in var_dcmd(var_rdmc(arg_rcsn)):
                var_rjut, var_lsgw = arg_rcsn[var_zbxo]
                var_cbvh = arg_bacg[var_zbxo]
                if var_wnki[var_rjut] * var_cbvh > var_wnki[var_lsgw]:
                    var_wnki[var_lsgw] = var_wnki[var_rjut] * var_cbvh
                    var_llti = 1
                if var_wnki[var_lsgw] * var_cbvh > var_wnki[var_rjut]:
                    var_wnki[var_rjut] = var_wnki[var_lsgw] * var_cbvh
                    var_llti = 1
            if not var_llti:
                break
        return var_wnki[arg_rgwu]
