class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = 0
        arg_xdvx.sort(key=lambda x: (var_rgwu[0], -var_rgwu[1]))
        for var_wrnh in var_osiz(var_ayzf(arg_xdvx) - 1):
            var_wnki = arg_xdvx[var_wrnh]
            var_egyk = var_wnki[0] - 1
            var_dcmd = var_llti.inf
            var_zbxo = -var_llti.inf
            var_rdmc = var_wnki[1] + 1
            for var_rjut in var_osiz(var_wrnh + 1, var_ayzf(arg_xdvx)):
                var_lsgw = arg_xdvx[var_rjut]
                if var_lsgw[0] > var_egyk and var_lsgw[0
                    ] < var_dcmd and var_lsgw[1] > var_zbxo and var_lsgw[1
                    ] < var_rdmc:
                    var_hqta += 1
                    var_egyk = var_lsgw[0]
                    var_zbxo = var_lsgw[1]
        return var_hqta
