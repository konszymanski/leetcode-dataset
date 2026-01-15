class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_rcsn[
        var_bacg]:
        var_hqta = []
        var_rgwu = var_wrnh('-inf')
        var_osiz = 0
        var_ayzf = var_wrnh('inf')
        for var_wnki in var_egyk(var_dcmd(arg_xdvx)):
            var_llti.heappush(var_hqta, (arg_xdvx[var_wnki][0], var_wnki, 0))
            var_rgwu = var_zbxo(var_rgwu, arg_xdvx[var_wnki][0])
        while var_dcmd(var_hqta) == var_dcmd(arg_xdvx):
            var_rdmc, var_rjut, var_lsgw = var_llti.heappop(var_hqta)
            if var_rgwu - var_rdmc < var_ayzf - var_osiz:
                var_osiz = var_rdmc
                var_ayzf = var_rgwu
            if var_lsgw + 1 < var_dcmd(arg_xdvx[var_rjut]):
                var_cbvh = arg_xdvx[var_rjut][var_lsgw + 1]
                var_llti.heappush(var_hqta, (var_cbvh, var_rjut, var_lsgw + 1))
                var_rgwu = var_zbxo(var_rgwu, var_cbvh)
        return [var_osiz, var_ayzf]
