class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_zbxo:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = [-1] * (var_bacg + 1)
        for var_wrnh in var_osiz(var_bacg):
            if var_wrnh == 0 or arg_xdvx[var_wrnh - 1] == '0':
                var_rgwu[var_wrnh + 1] = var_wrnh
            else:
                var_rgwu[var_wrnh + 1] = var_rgwu[var_wrnh]
        var_ayzf = 0
        for var_wrnh in var_osiz(1, var_bacg + 1):
            var_wnki = 1 if arg_xdvx[var_wrnh - 1] == '0' else 0
            var_egyk = var_wrnh
            while var_egyk > 0 and var_wnki * var_wnki <= var_bacg:
                var_dcmd = var_wrnh - var_rgwu[var_egyk] - var_wnki
                if var_wnki * var_wnki <= var_dcmd:
                    var_ayzf += var_llti(var_egyk - var_rgwu[var_egyk], 
                        var_dcmd - var_wnki * var_wnki + 1)
                var_egyk = var_rgwu[var_egyk]
                var_wnki += 1
        return var_ayzf
