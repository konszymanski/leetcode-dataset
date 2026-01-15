class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = var_wrnh(var_osiz)
        for var_ayzf, var_wnki in arg_rcsn:
            var_rgwu[var_ayzf].append(var_wnki)
            var_rgwu[var_wnki].append(var_ayzf)
        var_egyk = 0
        var_dcmd = var_llti()

        def func_zbxo(arg_rdmc: var_bacg, arg_rjut: var_osiz) ->None:
            var_dcmd.add(arg_rdmc)
            arg_rjut[0] += 1
            arg_rjut[1] += var_lsgw(var_rgwu[arg_rdmc])
            for var_cbvh in var_rgwu[arg_rdmc]:
                if var_cbvh not in var_dcmd:
                    func_zbxo(var_cbvh, arg_rjut)
        for var_yjch in var_dmio(arg_xdvx):
            if var_yjch in var_dcmd:
                continue
            var_ulfl = [0, 0]
            func_zbxo(var_yjch, var_ulfl)
            if var_ulfl[0] * (var_ulfl[0] - 1) == var_ulfl[1]:
                var_egyk += 1
        return var_egyk
