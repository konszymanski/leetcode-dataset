class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu = [(-var_wrnh, var_wrnh, 1) for var_wrnh in arg_rcsn]
        var_osiz.heapify(var_rgwu)
        for var_ayzf in var_wnki(arg_xdvx - var_bacg):
            var_egyk, var_dcmd, var_llti = var_osiz.heappop(var_rgwu)
            var_zbxo = var_llti + 1
            var_rdmc = var_dcmd / var_zbxo
            var_osiz.heappush(var_rgwu, (-var_rdmc, var_dcmd, var_zbxo))
        var_ayzf, var_dcmd, var_llti = var_osiz.heappop(var_rgwu)
        return var_rjut.ceil(var_dcmd / var_llti)
