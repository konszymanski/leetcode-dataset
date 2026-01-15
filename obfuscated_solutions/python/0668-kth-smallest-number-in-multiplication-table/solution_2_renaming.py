class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        var_rgwu = [(var_wrnh, var_wrnh) for var_wrnh in var_osiz(1, 
            arg_rcsn + 1)]
        var_ayzf.heapify(var_rgwu)
        for var_wnki in var_egyk(arg_hqta):
            var_dcmd, var_llti = var_ayzf.heappop(var_rgwu)
            var_zbxo = var_dcmd + var_llti
            if var_zbxo <= var_llti * arg_bacg:
                var_ayzf.heappush(var_rgwu, (var_zbxo, var_llti))
        return var_dcmd
