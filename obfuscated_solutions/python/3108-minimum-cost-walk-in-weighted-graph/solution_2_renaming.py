class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg):
        var_hqta = [[] for var_rgwu in var_wrnh(arg_xdvx)]
        for var_osiz in arg_rcsn:
            var_hqta[var_osiz[0]].append((var_osiz[1], var_osiz[2]))
            var_hqta[var_osiz[1]].append((var_osiz[0], var_osiz[2]))
        var_ayzf = [False] * arg_xdvx
        var_wnki = [0] * arg_xdvx
        var_egyk = []
        var_dcmd = 0
        for var_llti in var_wrnh(arg_xdvx):
            if not var_ayzf[var_llti]:
                var_egyk.append(arg_ihhe._get_component_cost(var_llti,
                    var_hqta, var_ayzf, var_wnki, var_dcmd))
                var_dcmd += 1
        var_zbxo = []
        for var_rdmc in arg_bacg:
            var_rjut, var_lsgw = var_rdmc
            if var_wnki[var_rjut] == var_wnki[var_lsgw]:
                var_zbxo.append(var_egyk[var_wnki[var_rjut]])
            else:
                var_zbxo.append(-1)
        return var_zbxo

    def func_cbvh(arg_ihhe, arg_yjch, var_hqta, var_ayzf, var_wnki, var_dcmd):
        var_dmio = var_ulfl()
        var_egyk = -1
        var_dmio.append(arg_yjch)
        var_ayzf[arg_yjch] = True
        while var_dmio:
            var_llti = var_dmio.popleft()
            var_wnki[var_llti] = var_dcmd
            for var_lgvi, var_wvuc in var_hqta[var_llti]:
                var_egyk &= var_wvuc
                if var_ayzf[var_lgvi]:
                    continue
                var_ayzf[var_lgvi] = True
                var_dmio.append(var_lgvi)
        return var_egyk
