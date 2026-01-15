class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_rgwu, arg_bacg: var_hqta[var_hqta[var_rgwu]]) ->var_rgwu:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = [([0] * 2) for var_wnki in var_egyk(var_wrnh + 1)]
        var_ayzf[var_wrnh][1] = 0
        var_ayzf[var_wrnh][0] = -var_dcmd('inf')
        for var_llti in var_egyk(var_wrnh - 1, -1, -1):
            for var_zbxo in var_egyk(2):
                var_rdmc = var_ayzf[var_llti + 1][var_zbxo ^ 1] + (arg_xdvx
                    [var_llti] ^ arg_rcsn)
                var_rjut = var_ayzf[var_llti + 1][var_zbxo] + arg_xdvx[var_llti
                    ]
                var_ayzf[var_llti][var_zbxo] = var_lsgw(var_rdmc, var_rjut)
        return var_ayzf[0][1]
