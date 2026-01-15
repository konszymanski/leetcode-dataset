class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_rgwu[var_rgwu[var_hqta]]) ->var_rgwu[
        var_rjut]:
        var_wrnh = [([False] * arg_xdvx) for var_osiz in var_ayzf(arg_xdvx)]
        for var_wnki in arg_rcsn:
            var_wrnh[var_wnki[0]][var_wnki[1]] = True
        for var_egyk in var_ayzf(arg_xdvx):
            for var_dcmd in var_ayzf(arg_xdvx):
                for var_llti in var_ayzf(arg_xdvx):
                    var_wrnh[var_dcmd][var_llti] = var_wrnh[var_dcmd][var_llti
                        ] or var_wrnh[var_dcmd][var_egyk] and var_wrnh[var_egyk
                        ][var_llti]
        var_zbxo = []
        for var_rdmc in arg_bacg:
            var_zbxo.append(var_wrnh[var_rdmc[0]][var_rdmc[1]])
        return var_zbxo
