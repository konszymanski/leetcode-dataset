class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_rcsn[var_bacg]]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = var_hqta * var_wrnh
        var_ayzf = [([var_osiz] * var_wrnh) for var_wnki in var_egyk(var_hqta)]
        for var_dcmd in var_egyk(var_hqta):
            for var_llti in var_egyk(var_wrnh):
                if arg_xdvx[var_dcmd][var_llti] == 1:
                    var_ayzf[var_dcmd][var_llti] = 0
        for var_dcmd in var_egyk(var_hqta):
            for var_llti in var_egyk(var_wrnh):
                var_zbxo = var_osiz
                var_rdmc = var_dcmd - 1
                var_rjut = var_llti
                if arg_ihhe.is_valid_cell(var_rdmc, var_rjut, var_hqta,
                    var_wrnh):
                    var_zbxo = var_lsgw(var_zbxo, var_ayzf[var_rdmc][var_rjut])
                var_rdmc = var_dcmd
                var_rjut = var_llti - 1
                if arg_ihhe.is_valid_cell(var_rdmc, var_rjut, var_hqta,
                    var_wrnh):
                    var_zbxo = var_lsgw(var_zbxo, var_ayzf[var_rdmc][var_rjut])
                var_ayzf[var_dcmd][var_llti] = var_lsgw(var_ayzf[var_dcmd][
                    var_llti], var_zbxo + 1)
        for var_dcmd in var_egyk(var_hqta - 1, -1, -1):
            for var_llti in var_egyk(var_wrnh - 1, -1, -1):
                var_zbxo = var_osiz
                var_rdmc = var_dcmd + 1
                var_rjut = var_llti
                if arg_ihhe.is_valid_cell(var_rdmc, var_rjut, var_hqta,
                    var_wrnh):
                    var_zbxo = var_lsgw(var_zbxo, var_ayzf[var_rdmc][var_rjut])
                var_rdmc = var_dcmd
                var_rjut = var_llti + 1
                if arg_ihhe.is_valid_cell(var_rdmc, var_rjut, var_hqta,
                    var_wrnh):
                    var_zbxo = var_lsgw(var_zbxo, var_ayzf[var_rdmc][var_rjut])
                var_ayzf[var_dcmd][var_llti] = var_lsgw(var_ayzf[var_dcmd][
                    var_llti], var_zbxo + 1)
        return var_ayzf

    def func_cbvh(arg_ihhe, var_dcmd: var_bacg, var_llti: var_bacg,
        var_hqta: var_bacg, var_wrnh: var_bacg) ->var_yjch:
        return 0 <= var_dcmd < var_hqta and 0 <= var_llti < var_wrnh
