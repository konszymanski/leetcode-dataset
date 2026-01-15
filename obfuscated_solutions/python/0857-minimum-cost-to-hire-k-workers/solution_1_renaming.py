class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_rgwu) ->var_wnki:
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = var_wnki('inf')
        var_egyk = 0
        var_dcmd = []
        for var_llti in var_zbxo(var_wrnh):
            var_dcmd.append((arg_rcsn[var_llti] / arg_xdvx[var_llti],
                arg_xdvx[var_llti]))
        var_dcmd.sort(key=lambda x: var_rdmc[0])
        var_rjut = []
        for var_llti in var_zbxo(var_wrnh):
            var_lsgw.heappush(var_rjut, -var_dcmd[var_llti][1])
            var_egyk += var_dcmd[var_llti][1]
            if var_osiz(var_rjut) > arg_bacg:
                var_egyk += var_lsgw.heappop(var_rjut)
            if var_osiz(var_rjut) == arg_bacg:
                var_ayzf = var_cbvh(var_ayzf, var_egyk * var_dcmd[var_llti][0])
        return var_ayzf
