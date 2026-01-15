class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_rcsn[var_zbxo]:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = []
        for var_osiz, arg_xdvx in var_ayzf(arg_xdvx):
            var_wnki.heappush(var_wrnh, (-arg_xdvx, var_osiz))
        var_egyk = [0] * var_hqta
        var_dcmd = 1
        while var_wrnh:
            var_llti = var_wnki.heappop(var_wrnh)[1]
            if var_dcmd == 1:
                var_egyk[var_llti] = 'Gold Medal'
            elif var_dcmd == 2:
                var_egyk[var_llti] = 'Silver Medal'
            elif var_dcmd == 3:
                var_egyk[var_llti] = 'Bronze Medal'
            else:
                var_egyk[var_llti] = var_zbxo(var_dcmd)
            var_dcmd += 1
        return var_egyk
