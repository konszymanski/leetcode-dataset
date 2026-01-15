class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_wrnh(arg_xdvx[0])
        var_ayzf = 0
        var_wnki = [(arg_bacg, arg_hqta)]
        arg_rcsn[arg_bacg][arg_hqta] = True
        var_egyk = [0, 0, 1, -1]
        var_dcmd = [1, -1, 0, 0]
        while var_wnki:
            arg_bacg, arg_hqta = var_wnki.pop(0)
            var_ayzf += arg_xdvx[arg_bacg][arg_hqta]
            for var_llti in var_zbxo(4):
                var_rdmc = arg_bacg + var_egyk[var_llti]
                var_rjut = arg_hqta + var_dcmd[var_llti]
                if (0 <= var_rdmc < var_rgwu and 0 <= var_rjut < var_osiz and
                    arg_xdvx[var_rdmc][var_rjut] and not arg_rcsn[var_rdmc]
                    [var_rjut]):
                    var_wnki.append((var_rdmc, var_rjut))
                    arg_rcsn[var_rdmc][var_rjut] = True
        return var_ayzf

    def func_lsgw(arg_ihhe, arg_xdvx):
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = var_wrnh(arg_xdvx[0])
        var_cbvh = 0
        arg_rcsn = [([False] * var_osiz) for var_yjch in var_zbxo(var_rgwu)]
        for var_llti in var_zbxo(var_rgwu):
            for var_dmio in var_zbxo(var_osiz):
                if arg_xdvx[var_llti][var_dmio] and not arg_rcsn[var_llti][
                    var_dmio]:
                    var_cbvh = var_ulfl(var_cbvh, arg_ihhe.count_fishes(
                        arg_xdvx, arg_rcsn, var_llti, var_dmio))
        return var_cbvh
