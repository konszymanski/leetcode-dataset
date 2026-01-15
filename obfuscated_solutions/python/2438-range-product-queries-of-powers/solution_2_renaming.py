class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_hqta[var_bacg]:
        var_rgwu = 10 ** 9 + 7
        var_wrnh, var_osiz = [], 1
        while arg_xdvx > 0:
            if arg_xdvx % 2 == 1:
                var_wrnh.append(var_osiz)
            arg_xdvx //= 2
            var_osiz *= 2
        var_ayzf = var_wnki(var_wrnh)
        var_egyk = [([0] * var_ayzf) for var_dcmd in var_llti(var_ayzf)]
        for var_zbxo in var_llti(var_ayzf):
            var_rdmc = 1
            for var_rjut in var_llti(var_zbxo, var_ayzf):
                var_rdmc = var_rdmc * var_wrnh[var_rjut] % var_rgwu
                var_egyk[var_zbxo][var_rjut] = var_rdmc
        var_lsgw = []
        for var_cbvh, var_yjch in arg_rcsn:
            var_lsgw.append(var_egyk[var_cbvh][var_yjch])
        return var_lsgw
