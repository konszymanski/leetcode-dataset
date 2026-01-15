class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = 10 ** 9 + 7
        var_wrnh, var_osiz = var_ayzf(arg_xdvx), 1
        var_wnki = var_egyk()
        for var_dcmd in var_llti(1, var_wrnh):
            if arg_xdvx[var_dcmd] == arg_xdvx[var_dcmd - 1]:
                var_osiz += 1
            else:
                var_wnki.append(var_osiz)
                var_osiz = 1
        var_wnki.append(var_osiz)
        var_zbxo = 1
        for var_rdmc in var_wnki:
            var_zbxo = var_zbxo * var_rdmc % var_rgwu
        if var_ayzf(var_wnki) >= arg_rcsn:
            return var_zbxo
        var_rjut, var_lsgw = [1] + [0] * (arg_rcsn - 1), [1] * arg_rcsn
        for var_dcmd in var_llti(var_ayzf(var_wnki)):
            var_cbvh = [0] * arg_rcsn
            for var_yjch in var_llti(1, arg_rcsn):
                var_cbvh[var_yjch] = var_lsgw[var_yjch - 1]
                if var_yjch - var_wnki[var_dcmd] - 1 >= 0:
                    var_cbvh[var_yjch] = (var_cbvh[var_yjch] - var_lsgw[
                        var_yjch - var_wnki[var_dcmd] - 1]) % var_rgwu
            var_dmio = [var_cbvh[0]] + [0] * (arg_rcsn - 1)
            for var_yjch in var_llti(1, arg_rcsn):
                var_dmio[var_yjch] = (var_dmio[var_yjch - 1] + var_cbvh[
                    var_yjch]) % var_rgwu
            var_rjut, var_lsgw = var_cbvh, var_dmio
        return (var_zbxo - var_lsgw[arg_rcsn - 1]) % var_rgwu
