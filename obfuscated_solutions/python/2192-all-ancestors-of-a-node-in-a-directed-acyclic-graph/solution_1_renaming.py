class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_hqta[var_hqta[var_bacg]]:
        var_rgwu = [[] for var_wrnh in var_osiz(arg_xdvx)]
        for var_ayzf, var_wnki in arg_rcsn:
            var_rgwu[var_wnki].append(var_ayzf)
        var_egyk = []
        for var_dcmd in var_osiz(arg_xdvx):
            var_llti = []
            var_zbxo = var_rdmc()
            arg_ihhe.find_children(var_dcmd, var_rgwu, var_zbxo)
            for var_rjut in var_osiz(arg_xdvx):
                if var_rjut == var_dcmd:
                    continue
                if var_rjut in var_zbxo:
                    var_llti.append(var_rjut)
            var_egyk.append(var_llti)
        return var_egyk

    def func_lsgw(arg_ihhe, arg_cbvh, var_rgwu, arg_yjch):
        arg_yjch.add(arg_cbvh)
        for var_dmio in var_rgwu[arg_cbvh]:
            if var_dmio not in arg_yjch:
                arg_ihhe.find_children(var_dmio, var_rgwu, arg_yjch)
