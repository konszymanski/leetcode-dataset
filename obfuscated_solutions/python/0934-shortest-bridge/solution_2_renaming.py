class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh, var_osiz = -1, -1
        for var_ayzf in var_wnki(var_hqta):
            for var_egyk in var_wnki(var_hqta):
                if arg_xdvx[var_ayzf][var_egyk] == 1:
                    var_wrnh, var_osiz = var_ayzf, var_egyk
                    break
        var_dcmd = [(var_wrnh, var_osiz)]
        var_llti = [(var_wrnh, var_osiz)]
        arg_xdvx[var_wrnh][var_osiz] = 2
        while var_dcmd:
            var_zbxo = []
            for var_rdmc, var_rjut in var_dcmd:
                for var_lsgw, var_cbvh in [(var_rdmc + 1, var_rjut), (
                    var_rdmc - 1, var_rjut), (var_rdmc, var_rjut + 1), (
                    var_rdmc, var_rjut - 1)]:
                    if (0 <= var_lsgw < var_hqta and 0 <= var_cbvh <
                        var_hqta and arg_xdvx[var_lsgw][var_cbvh] == 1):
                        var_zbxo.append((var_lsgw, var_cbvh))
                        var_llti.append((var_lsgw, var_cbvh))
                        arg_xdvx[var_lsgw][var_cbvh] = 2
            var_dcmd = var_zbxo
        var_yjch = 0
        while var_llti:
            var_zbxo = []
            for var_rdmc, var_rjut in var_llti:
                for var_lsgw, var_cbvh in [(var_rdmc + 1, var_rjut), (
                    var_rdmc - 1, var_rjut), (var_rdmc, var_rjut + 1), (
                    var_rdmc, var_rjut - 1)]:
                    if 0 <= var_lsgw < var_hqta and 0 <= var_cbvh < var_hqta:
                        if arg_xdvx[var_lsgw][var_cbvh] == 1:
                            return var_yjch
                        elif arg_xdvx[var_lsgw][var_cbvh] == 0:
                            var_zbxo.append((var_lsgw, var_cbvh))
                            arg_xdvx[var_lsgw][var_cbvh] = -1
            var_llti = var_zbxo
            var_yjch += 1
        return var_yjch
