class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = arg_xdvx[arg_rcsn][0]
        arg_xdvx = var_wrnh([(var_osiz, var_ayzf, var_wnki) for var_wnki, (
            var_osiz, var_ayzf) in var_egyk(arg_xdvx)])
        var_dcmd = 0
        var_llti = []
        var_zbxo = []
        for var_rdmc in arg_xdvx:
            var_osiz, var_ayzf, var_wnki = var_rdmc
            while var_zbxo and var_zbxo[0][0] <= var_osiz:
                var_rjut, var_lsgw = var_cbvh.heappop(var_zbxo)
                var_cbvh.heappush(var_llti, var_lsgw)
            if var_llti:
                var_yjch = var_cbvh.heappop(var_llti)
            else:
                var_yjch = var_dcmd
                var_dcmd += 1
            var_cbvh.heappush(var_zbxo, (var_ayzf, var_yjch))
            if var_wnki == arg_rcsn:
                return var_yjch
        return 0
