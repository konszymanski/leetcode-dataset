class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = [[] for var_wrnh in var_osiz(arg_xdvx)]
        for var_ayzf, var_wnki in arg_rcsn:
            var_rgwu[var_ayzf].append(var_wnki)
            var_rgwu[var_wnki].append(var_ayzf)
        var_egyk = [False] * arg_xdvx
        var_dcmd = 0
        for var_llti in var_osiz(arg_xdvx):
            if not var_egyk[var_llti]:
                var_zbxo = []
                var_rdmc = [var_llti]
                var_egyk[var_llti] = True
                while var_rdmc:
                    var_rjut = var_rdmc.pop(0)
                    var_zbxo.append(var_rjut)
                    for var_lsgw in var_rgwu[var_rjut]:
                        if not var_egyk[var_lsgw]:
                            var_rdmc.append(var_lsgw)
                            var_egyk[var_lsgw] = True
                var_cbvh = True
                for var_yjch in var_zbxo:
                    if var_dmio(var_rgwu[var_yjch]) != var_dmio(var_zbxo) - 1:
                        var_cbvh = False
                        break
                if var_cbvh:
                    var_dcmd += 1
        return var_dcmd
