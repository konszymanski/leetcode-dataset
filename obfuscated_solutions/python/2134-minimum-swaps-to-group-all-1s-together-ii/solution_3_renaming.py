class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = var_rgwu('inf')
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = arg_xdvx[0]
        var_wnki = 0
        for var_egyk in var_dcmd(var_llti(arg_xdvx)):
            if var_egyk != 0:
                var_ayzf -= arg_xdvx[var_egyk - 1]
            while var_wnki - var_egyk + 1 < var_wrnh:
                var_wnki += 1
                var_ayzf += arg_xdvx[var_wnki % var_llti(arg_xdvx)]
            var_hqta = var_zbxo(var_hqta, var_wrnh - var_ayzf)
        return var_hqta
