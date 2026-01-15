class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 10 ** 9 + 7
        var_rgwu = var_wrnh(var_osiz)
        for var_ayzf, var_wnki in var_egyk(arg_xdvx):
            var_rgwu[var_wnki].append(var_ayzf)

        def func_dcmd(arg_llti, var_ayzf):
            var_zbxo, var_rdmc = 0, var_rjut(arg_llti) - 1
            while var_zbxo < var_rdmc:
                var_lsgw = var_zbxo + (var_rdmc - var_zbxo + 1 >> 1)
                if var_ayzf >= arg_llti[var_lsgw]:
                    var_zbxo = var_lsgw
                else:
                    var_rdmc = var_lsgw - 1
            return var_zbxo + 1, var_rjut(arg_llti) - 1 - var_zbxo
        var_cbvh = 0
        for var_ayzf in var_yjch(1, var_rjut(arg_xdvx) - 1):
            var_dmio = arg_xdvx[var_ayzf] * 2
            if var_dmio in var_rgwu and var_rjut(var_rgwu[var_dmio]
                ) > 1 and var_rgwu[var_dmio][0] < var_ayzf:
                var_zbxo, var_rdmc = func_dcmd(var_rgwu[var_dmio], var_ayzf)
                if arg_xdvx[var_ayzf] == 0:
                    var_zbxo -= 1
                var_cbvh = (var_cbvh + var_zbxo * var_rdmc) % var_hqta
        return var_cbvh
