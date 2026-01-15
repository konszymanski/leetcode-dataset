class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = [False] * arg_xdvx
        var_wrnh = var_osiz()
        var_wrnh.append(0)
        var_rgwu[0] = True
        var_ayzf = 1
        var_wnki = 0
        var_egyk = 0
        while var_wrnh:
            for var_dcmd in var_llti(var_ayzf):
                var_zbxo = var_wrnh.popleft()
                if var_zbxo == arg_xdvx - 1:
                    return var_egyk
                for var_rdmc in arg_rcsn[var_zbxo]:
                    if var_rgwu[var_rdmc]:
                        continue
                    var_wrnh.append(var_rdmc)
                    var_wnki += 1
                    var_rgwu[var_rdmc] = True
            var_ayzf = var_wnki
            var_wnki = 0
            var_egyk += 1
        return -1

    def func_rjut(arg_ihhe, arg_xdvx: var_bacg, arg_lsgw: var_hqta[var_hqta
        [var_bacg]]) ->var_hqta[var_bacg]:
        var_cbvh = []
        arg_rcsn = [[] for var_dcmd in var_llti(arg_xdvx)]
        for var_yjch in var_llti(arg_xdvx - 1):
            arg_rcsn[var_yjch].append(var_yjch + 1)
        for var_dmio in arg_lsgw:
            var_ulfl, var_lgvi = var_dmio
            arg_rcsn[var_ulfl].append(var_lgvi)
            var_cbvh.append(arg_ihhe.bfs(arg_xdvx, arg_rcsn))
        return var_cbvh
