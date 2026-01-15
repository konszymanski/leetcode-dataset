class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_hqta) ->var_cbvh:

        def func_rgwu(arg_wrnh, arg_osiz):
            return (arg_wrnh + 1) / (arg_osiz + 1) - arg_wrnh / arg_osiz
        var_ayzf = []
        for arg_wrnh, arg_osiz in arg_xdvx:
            var_wnki = func_rgwu(arg_wrnh, arg_osiz)
            var_ayzf.append((-var_wnki, arg_wrnh, arg_osiz))
        var_egyk.heapify(var_ayzf)
        for var_dcmd in var_llti(arg_rcsn):
            var_zbxo, arg_wrnh, arg_osiz = var_egyk.heappop(var_ayzf)
            var_egyk.heappush(var_ayzf, (-func_rgwu(arg_wrnh + 1, arg_osiz +
                1), arg_wrnh + 1, arg_osiz + 1))
        var_rdmc = var_rjut(arg_wrnh / arg_osiz for var_dcmd, arg_wrnh,
            arg_osiz in var_ayzf)
        return var_rdmc / var_lsgw(arg_xdvx)
