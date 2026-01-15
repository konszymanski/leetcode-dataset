class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta, var_rgwu = var_wrnh(arg_xdvx), var_wrnh(arg_xdvx) // 3
        var_osiz = [0] * (var_rgwu + 1)
        var_ayzf = var_wnki(arg_xdvx[:var_rgwu])
        var_egyk = [(-var_dcmd) for var_dcmd in arg_xdvx[:var_rgwu]]
        var_llti.heapify(var_egyk)
        var_osiz[0] = var_ayzf
        for var_zbxo in var_rdmc(var_rgwu, var_rgwu * 2):
            var_ayzf += arg_xdvx[var_zbxo]
            var_llti.heappush(var_egyk, -arg_xdvx[var_zbxo])
            var_ayzf -= -var_llti.heappop(var_egyk)
            var_osiz[var_zbxo - (var_rgwu - 1)] = var_ayzf
        var_rjut = var_wnki(arg_xdvx[var_rgwu * 2:])
        var_lsgw = arg_xdvx[var_rgwu * 2:]
        var_llti.heapify(var_lsgw)
        var_cbvh = var_osiz[var_rgwu] - var_rjut
        for var_zbxo in var_rdmc(var_rgwu * 2 - 1, var_rgwu - 1, -1):
            var_rjut += arg_xdvx[var_zbxo]
            var_llti.heappush(var_lsgw, arg_xdvx[var_zbxo])
            var_rjut -= var_llti.heappop(var_lsgw)
            var_cbvh = var_yjch(var_cbvh, var_osiz[var_zbxo - var_rgwu] -
                var_rjut)
        return var_cbvh
