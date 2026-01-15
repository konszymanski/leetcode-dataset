class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_hqta) ->var_rgwu[var_hqta]:
        arg_rcsn.sort(key=lambda x: var_wrnh[2])
        var_osiz = var_ayzf(var_wnki)
        for var_wrnh, var_egyk, var_dcmd in arg_rcsn:
            var_osiz[var_dcmd].append((var_wrnh, var_egyk))
        var_llti = [False] * arg_xdvx
        var_llti[0] = True
        var_llti[arg_bacg] = True
        for var_dcmd in var_osiz:
            var_zbxo = var_ayzf(var_wnki)
            for var_wrnh, var_egyk in var_osiz[var_dcmd]:
                var_zbxo[var_wrnh].append(var_egyk)
                var_zbxo[var_egyk].append(var_wrnh)
            var_rdmc = var_rjut()
            for var_wrnh, var_egyk in var_osiz[var_dcmd]:
                if var_llti[var_wrnh]:
                    var_rdmc.add(var_wrnh)
                if var_llti[var_egyk]:
                    var_rdmc.add(var_egyk)
            var_rdmc = var_lsgw(var_rdmc)
            while var_rdmc:
                var_cbvh = var_rdmc.popleft()
                for var_yjch in var_zbxo[var_cbvh]:
                    if not var_llti[var_yjch]:
                        var_llti[var_yjch] = True
                        var_rdmc.append(var_yjch)
        return [var_dmio for var_dmio in var_ulfl(arg_xdvx) if var_llti[
            var_dmio]]
