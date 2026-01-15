class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = [0] * var_rgwu(arg_xdvx[0])
        var_wrnh = 0
        for var_osiz in arg_xdvx:
            for var_ayzf, var_wnki in var_egyk(var_osiz):
                var_hqta[var_ayzf] = 0 if var_wnki == 0 else var_hqta[var_ayzf
                    ] + 1
            var_dcmd = [[-1, 0, -1]]
            for var_ayzf, var_llti in var_egyk(var_hqta):
                while var_dcmd[-1][2] >= var_llti:
                    var_dcmd.pop()
                var_zbxo, var_rdmc, var_rjut = var_dcmd[-1]
                var_lsgw = var_rdmc + (var_ayzf - var_zbxo) * var_llti
                var_dcmd.append([var_ayzf, var_lsgw, var_llti])
                var_wrnh += var_lsgw
        return var_wrnh
