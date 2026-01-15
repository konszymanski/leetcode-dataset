class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = 1000000007
        var_wrnh = [[] for var_osiz in var_ayzf(arg_xdvx)]
        for var_wnki, var_egyk, var_dcmd in arg_rcsn:
            var_wrnh[var_wnki].append((var_egyk, var_dcmd))
            var_wrnh[var_egyk].append((var_wnki, var_dcmd))
        var_llti = [(0, 0)]
        var_zbxo = [var_rdmc('inf')] * arg_xdvx
        var_rjut = [0] * arg_xdvx
        var_zbxo[0] = 0
        var_rjut[0] = 1
        while var_llti:
            var_lsgw, var_cbvh = var_yjch.heappop(var_llti)
            if var_lsgw > var_zbxo[var_cbvh]:
                continue
            for var_dmio, var_ulfl in var_wrnh[var_cbvh]:
                if var_lsgw + var_ulfl < var_zbxo[var_dmio]:
                    var_zbxo[var_dmio] = var_lsgw + var_ulfl
                    var_rjut[var_dmio] = var_rjut[var_cbvh]
                    var_yjch.heappush(var_llti, (var_zbxo[var_dmio], var_dmio))
                elif var_lsgw + var_ulfl == var_zbxo[var_dmio]:
                    var_rjut[var_dmio] = (var_rjut[var_dmio] + var_rjut[
                        var_cbvh]) % var_rgwu
        return var_rjut[arg_xdvx - 1]
