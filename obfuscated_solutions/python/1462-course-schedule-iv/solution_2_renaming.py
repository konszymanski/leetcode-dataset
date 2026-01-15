class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_wrnh[var_wrnh
        [var_rgwu]], arg_bacg: var_osiz[var_rgwu, var_wrnh[var_rgwu]],
        arg_hqta: var_wrnh[var_wrnh[var_ayzf]]) ->None:
        for var_wnki in var_egyk(arg_xdvx):
            var_dcmd = var_llti([var_wnki])
            while var_dcmd:
                var_zbxo = var_dcmd.popleft()
                for var_rdmc in arg_bacg.get(var_zbxo, []):
                    if not arg_hqta[var_wnki][var_rdmc]:
                        arg_hqta[var_wnki][var_rdmc] = True
                        var_dcmd.append(var_rdmc)

    def func_rjut(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_wrnh[var_wrnh
        [var_rgwu]], arg_lsgw: var_wrnh[var_wrnh[var_rgwu]]) ->var_wrnh[
        var_ayzf]:
        arg_bacg = {}
        for var_cbvh in arg_rcsn:
            if var_cbvh[0] not in arg_bacg:
                arg_bacg[var_cbvh[0]] = []
            arg_bacg[var_cbvh[0]].append(var_cbvh[1])
        arg_hqta = [([False] * arg_xdvx) for var_yjch in var_egyk(arg_xdvx)]
        arg_ihhe.preprocess(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta)
        var_dmio = []
        for var_ulfl in arg_lsgw:
            var_dmio.append(arg_hqta[var_ulfl[0]][var_ulfl[1]])
        return var_dmio
