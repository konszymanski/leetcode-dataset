class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx[0])
        var_osiz = 0
        var_ayzf = [([0] * var_rgwu) for var_wnki in var_egyk(var_hqta)]
        for var_dcmd in var_egyk(var_hqta):
            for var_llti in var_egyk(var_rgwu):
                if var_llti == 0:
                    var_ayzf[var_dcmd][var_llti] = arg_xdvx[var_dcmd][var_llti]
                else:
                    var_ayzf[var_dcmd][var_llti] = 0 if arg_xdvx[var_dcmd][
                        var_llti] == 0 else var_ayzf[var_dcmd][var_llti - 1
                        ] + 1
                var_zbxo = var_ayzf[var_dcmd][var_llti]
                for var_rdmc in var_egyk(var_dcmd, -1, -1):
                    var_zbxo = var_rjut(var_zbxo, var_ayzf[var_rdmc][var_llti])
                    if var_zbxo == 0:
                        break
                    var_osiz += var_zbxo
        return var_osiz
